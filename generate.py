import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime
import re

URL = "https://www.wembleystadium.com/events"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

cal = Calendar()

# Each event card has this content structure
cards = soup.find_all(string=re.compile(r"\d{1,2}\s+\w+\s+\d{4}"))

events_added = 0

for date_text in cards:

    parent = date_text.find_parent()

    if not parent:
        continue

    block = parent.get_text(" ", strip=True)

    # Extract date
    match = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", block)
    if not match:
        continue

    try:
        date = datetime.strptime(match.group(1), "%d %b %Y")
    except:
        continue

    # Split lines of text from the card
    parts = block.split()

    # Attempt to find title (usually ALL CAPS words after date/time)
    title_match = re.search(
        r"\d{1,2}\s+\w+\s+\d{4}\s+\d{2}:\d{2}\s+([A-Z0-9\s\-]+)",
        block
    )

    if not title_match:
        continue

    title = title_match.group(1).strip()

    # Attempt to find subtitle (teams etc.)
    desc_match = re.search(rf"{re.escape(title)}\s+(.*?)\s+(FIND OUT MORE|BUY TICKETS|COMING SOON)", block)

    description = desc_match.group(1).strip() if desc_match else ""

    e = Event()
    e.name = title.title()
    e.begin = date
    e.duration = {"hours": 3}
    e.location = "Wembley Stadium, London, UK"
    e.description = description

    cal.events.add(e)
    events_added += 1

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {events_added} events")
