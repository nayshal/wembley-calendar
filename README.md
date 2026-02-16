# Wembley Stadium Events Calendar (Auto-Updating)

A free, auto-updating calendar subscription for all events at Wembley Stadium.

This project scrapes the official Wembley Stadium events page and generates a live `.ics` calendar feed that works with Apple Calendar, Google Calendar, Outlook, and most calendar apps.

## Live Calendar Feed

https://nayshal.github.io/wembley-calendar/wembley.ics

Subscribe to this URL — do NOT download it.

---

## Features

- Auto-updates daily via GitHub Actions
- Includes all upcoming Wembley Stadium events
- All-day events for clean display
- Removes duplicate “Away Supporters” listings
- Includes event descriptions
- Includes direct link to official event page
- Map-ready location (Wembley Stadium)
- Works on iPhone, Android, Google Calendar, Outlook, etc.
- No API keys required
- Completely free

---

## How It Works

1. A Python script scrapes the official events page:
   https://www.wembleystadium.com/events

2. It extracts:
   - Event title
   - Date
   - Description
   - Event page link
   - Venue location

3. The script generates a standard iCalendar (`.ics`) file.

4. GitHub Actions runs automatically (daily) and updates the file.

5. GitHub Pages hosts the `.ics` file publicly.

Your calendar app periodically refreshes the feed.

---

## Subscribe on iPhone / iPad (Apple Calendar)

1. Open Settings
2. Tap Calendar
3. Tap Accounts
4. Tap Add Account
5. Tap Other
6. Tap Add Subscribed Calendar
7. Paste the URL:

   https://nayshal.github.io/wembley-calendar/wembley.ics

8. Tap Next → Save

---

## Subscribe on Android (Google Calendar)

1. Open https://calendar.google.com in a browser
2. In the left sidebar, click + next to "Other calendars"
3. Select From URL
4. Paste:

   https://nayshal.github.io/wembley-calendar/wembley.ics

5. Click Add calendar

The calendar will sync to your phone automatically.

---

## Subscribe in Outlook

### Outlook Web / Office 365

1. Open Outlook Calendar
2. Click Add calendar
3. Choose Subscribe from web
4. Paste the URL
5. Name the calendar
6. Click Import

### Outlook Desktop

1. Go to Calendar view
2. Select Add Calendar → From Internet
3. Paste the URL
4. Confirm

---

## Subscribe on macOS (Apple Calendar)

1. Open Calendar app
2. File → New Calendar Subscription
3. Paste the URL
4. Configure refresh settings
5. Click OK

---

## Refresh Behavior

Calendar subscriptions update automatically.

Typical refresh intervals:

- Apple Calendar: every few hours to daily
- Google Calendar: ~8–24 hours
- Outlook: varies

To force refresh, remove and re-add the subscription.

---

## Running Your Own Version

Requirements:

- Python 3
- requests
- beautifulsoup4
- ics

Install locally:

pip install -r requirements.txt

Run:

python generate.py

---

## Automation

GitHub Actions runs the script automatically on a schedule and commits updates to the repository.

GitHub Pages serves the updated `.ics` file publicly.

---

## Limitations

- Event times are not included (all-day events for consistency)
- Calendar apps control refresh frequency
- Some apps may not display venue photos for subscribed calendars
- Events depend on data published on the official Wembley site

---

## Disclaimer

This project is not affiliated with Wembley Stadium.  
All event data comes from the public website.

---

## License

MIT License — free to use and modify.
