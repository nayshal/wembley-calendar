import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime, date
import re

URL = "https://www.wembleystadium.com/events"
BASE = "https://www.wembleystadium.com"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

cal = Calendar()

seen_titles = set()

for heading in soup.find_all(["h2", "h3"]):

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

    # 📝 Extract description (text after title)
    after_title = text.split(title, 1)[-1]
    desc_match = re.search(r"([A-Za-z0-9 ,.'\-]{5,})", after_title)
    description = desc_match.group(1).strip() if desc_match else ""

    # 🔗 Find event page link
    link_el = card.find("a", href=True)
    event_url = BASE + link_el["href"] if link_el else URL

    e = Event()
    e.name = title.title()

    # ⭐ ALL-DAY EVENT
    e.begin = date(dt.year, dt.month, dt.day)

    # 📍 Map-ready address
    e.location = "Wembley Stadium, London HA9 0WS, United Kingdom"

    # 📝 Description + link (tapable on iPhone)
    e.description = f"{description}\n\nEvent details:\n{event_url}"

    cal.events.add(e)

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {len(cal.events)} events")
