import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime

URL = "https://www.wembleystadium.com/events"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

cal = Calendar()

for item in soup.select("a[href*='/events/']"):
    title = item.get_text(strip=True)

    # Attempt to find nearby date text
    parent = item.find_parent()
    date_text = parent.get_text(" ", strip=True)

    # Very basic date extraction (Wembley uses formats like "22 Mar 2026")
    import re
    match = re.search(r"\d{1,2}\s+\w+\s+\d{4}", date_text)

    if match:
        try:
            date = datetime.strptime(match.group(), "%d %b %Y")

            e = Event()
            e.name = title
            e.begin = date
            e.duration = {"hours": 3}

            cal.events.add(e)

        except:
            pass

with open("wembley.ics", "w") as f:
    f.writelines(cal)
