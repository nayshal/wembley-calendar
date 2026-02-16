import requests
from ics import Calendar, Event
from datetime import datetime
import re

URL = "https://www.wembleystadium.com/events"

r = requests.get(URL)
html = r.text

cal = Calendar()

# Find dates like "22 Mar 2026"
date_matches = re.findall(r"\d{1,2}\s+\w+\s+\d{4}", html)

# Find event titles near those dates
title_matches = re.findall(
    r'aria-label="([^"]+)"', html
)

events_added = 0

for title, date_str in zip(title_matches, date_matches):

    try:
        date = datetime.strptime(date_str, "%d %b %Y")
    except:
        continue

    e = Event()
    e.name = title
    e.begin = date
    e.duration = {"hours": 3}
    e.location = "Wembley Stadium, London, UK"
    e.description = f"{title}\n\nhttps://www.wembleystadium.com/events"

    cal.events.add(e)
    events_added += 1

with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {events_added} events")
