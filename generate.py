import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime
import re

URL = "https://www.wembleystadium.com/events"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

cal = Calendar()

# Wembley event cards contain the event title in <h3>
cards = soup.select("div.event-item, li.event-item, article")

for card in cards:

    title_el = card.find(["h2", "h3"])
    if not title_el:
        continue

    title = title_el.get_text(strip=True)

    text = card.get_text(" ", strip=True)

    # Extract date like "22 Mar 2026"
    match = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", text)
    if not match:
        continue

    try:
        date = datetime.strptime(match.group(1), "%d %b %Y")
    except:
        continue

    # Find link to event page
    link_el = card.find("a", href=True)
    event_url = ""
    if link_el:
        event_url = "https://www.wembleystadium.com" + link_el["href"]

    e = Event()
    e.name = title
    e.begin = date
    e.duration = {"hours": 3}
    e.location = "Wembley Stadium, London, UK"
    e.description = f"{title}\n\n{event_url}"

    cal.events.add(e)

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {len(cal.events)} events")
