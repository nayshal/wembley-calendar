import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime, date
import re

BASE = "https://www.wembleystadium.com"
URL = BASE + "/events"

cal = Calendar()
seen = set()

page = 1

while True:
    r = requests.get(f"{URL}?page={page}")
    soup = BeautifulSoup(r.text, "html.parser")

    headings = soup.find_all(["h2", "h3"])
    if not headings:
        break

    added_on_page = 0

    for heading in headings:

        title = heading.get_text(strip=True)

        if not title or len(title) < 5:
            continue

        # Skip away-supporter listings
        if re.search(r"AWAY|SUPPORTER", title, re.IGNORECASE):
            continue

        card = heading.find_parent()
        if not card:
            continue

        text = card.get_text(" ", strip=True)

        # Extract date
        date_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", text)
        if not date_match:
            continue

        try:
            dt = datetime.strptime(date_match.group(1), "%d %b %Y")
        except:
            continue

        key = (title, dt.date())
        if key in seen:
            continue
        seen.add(key)

        # Clean description (remove button text)
        after_title = text.split(title, 1)[-1]
        description = re.sub(
            r"(FIND OUT MORE|BUY TICKETS|BUY HOSPITALITY|COMING SOON)",
            "",
            after_title,
            flags=re.IGNORECASE
        ).strip()

        # Event link
        link_el = card.find("a", href=True)
        event_url = BASE + link_el["href"] if link_el else URL

        e = Event()
        e.name = title.title()

        # True all-day
        e.begin = date(dt.year, dt.month, dt.day)
        e.make_all_day()

        # Location name only
        e.location = "Wembley Stadium"

        # ⭐ Proper geographic coordinates
        e.geo = (51.5560, -0.2796)

        # Description + link
        e.description = f"{description}\n\nEvent details:\n{event_url}"

        cal.events.add(e)
        added_on_page += 1

    if added_on_page == 0:
        break

    page += 1

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {len(cal.events)} events")
