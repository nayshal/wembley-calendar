import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime
import re

URL = "https://www.wembleystadium.com/events"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

cal = Calendar()

events_found = 0

for text in soup.stripped_strings:
    match = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", text)

    if match:
        try:
            date = datetime.strptime(match.group(1), "%d %b %Y")

            e = Event()
            e.name = "Wembley Stadium Event"
            e.begin = date
            e.duration = {"hours": 3}

            cal.events.add(e)
            events_found += 1

        except:
            pass

# ALWAYS write the file (even if empty)
with open("wembley.ics", "w") as f:
    f.writelines(cal)

print(f"Created calendar with {events_found} events")
