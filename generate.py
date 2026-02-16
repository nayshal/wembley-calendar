import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime, date
import re

BASE = "https://www.wembleystadium.com"
URL = BASE + "/events"

cal = Calendar()
seen_titles = set()

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

        # ❌ Skip away-supporter versions
        if re.search(r"AWAY|SUPPORTER", title, re.IGNORECASE):
            continue

        card = heading.find_parent()
        if not card:
            continue

        text = card.get_text(" ", strip=True)

        # 📅 Extract date
        date_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", text)
        if not date_match:
            continue

        try:
            dt = datetime.strptime(date_match.group(1), "%d %b %Y")
        except:
            continue

        # 🚫 Prevent duplicates
        if title in seen_titles:
            continue
        seen_titles.add(title)

        # 📝 Description
        after_title = text.split(title, 1)[-1]
        desc_match = re.search(r"([A-Za-z0-9 ,.'\-]{5,})", after_title)
        description = desc_match.group(1).strip() if desc_match else ""

        # 🔗 Event link
        link_el = card.find("a", href=True)
        event_url = BASE + link_el["href"] if link_el else URL

        e = Event()
        e.name = title.title()

        # ⭐ Set date FIRST
        e.begin = date(dt.year, dt.month, dt.day)

        # ⭐ THEN convert to all-day
        e.make_all_day()

        # 📍 Location
        e.location = "Wembley Stadium"

        # 📝 Description + link
        e.description = f"{description}\n\nEvent details:\n{event_url}"

        cal.events.add(e)
        added_on_page += 1

    if added_on_page == 0:
        break

    page += 1

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {len(cal.events)} events")
