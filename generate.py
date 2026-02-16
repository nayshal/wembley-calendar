import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime
import re

URL = "https://www.wembleystadium.com/events"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

cal = Calendar()

# Wembley event titles are inside headings on event cards
for heading in soup.find_all(["h2", "h3"]):

    title = heading.get_text(strip=True)

    # Skip non-event headings
    if not title or len(title) < 5:
        continue

    card = heading.find_parent()

    if not card:
        continue

    text = card.get_text(" ", strip=True)

    # Find date like "22 Mar 2026"
    date_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", text)
    if not date_match:
        continue

    try:
        date = datetime.strptime(date_match.group(1), "%d %b %Y")
    except:
        continue

    # Try to find subtitle (teams etc.)
    # Usually appears right after title
    after_title = text.split(title, 1)[-1]

    desc_match = re.search(r"([A-Za-z0-9 vV\-\']{3,})", after_title)

    description = desc_match.group(1).strip() if desc_match else ""

    e = Event()
    e.name = title.title()
    e.begin = date
    e.duration = {"hours": 3}
    e.location = "Wembley Stadium, London, UK"
    e.description = description

    cal.events.add(e)

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {len(cal.events)} events")
