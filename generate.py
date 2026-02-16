import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime
import re

URL = "https://www.wembleystadium.com/events"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

cal = Calendar()

for link in soup.select("a[href*='/events/']"):

    title = link.get_text(strip=True)

    if not title:
        continue

    parent = link.find_parent()

    text = parent.get_text(" ", strip=True)

    match = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", text)

    if not match:
        continue

    try:
        date = datetime.strptime(match.group(1), "%d %b %Y")
    except:
        continue

    event_url = "https://www.wembleystadium.com" + link["href"]

    e = Event()
    e.name = title
    e.begin = date
    e.duration = {"hours": 3}

    # 📍 Location
    e.location = "Wembley Stadium, London, UK"

    # 📝 Description (shows on iPhone)
    e.description = f"{title}\n\nWembley Stadium\n{event_url}"

    cal.events.add(e)

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {len(cal.events)} events")
