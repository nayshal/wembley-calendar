# 🏟️ Wembley Stadium Events Calendar

<p align="center">
  <b>📅 Auto‑updating subscription calendar for all Wembley Stadium events</b><br>
  Concerts • Football • Finals • Special events
</p>

<p align="center">
  <a href="https://github.com/nayshal/wembley-calendar/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/nayshal/wembley-calendar/update.yml?label=Build&logo=github&style=for-the-badge" />
  </a>
  <img src="https://img.shields.io/badge/Auto--Update-Daily-blue?style=for-the-badge&logo=clockify" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-iOS%20%7C%20Android%20%7C%20Outlook-orange?style=for-the-badge" />
</p>

---

## ✨ Live Calendar Feed

👉 **Subscribe here:**  
https://nayshal.github.io/wembley-calendar/wembley.ics

> ⚠️ Subscribe to the URL — do NOT download the file.

---

## 🚀 Features

- 📡 Fully automatic updates (GitHub Actions)
- 📅 All upcoming Wembley Stadium events
- 🌙 Clean all‑day entries
- 🏟️ Map‑ready location (Wembley Stadium)
- 🔗 Direct links to official event pages
- 🧹 Removes duplicate “Away Supporters” listings
- 📱 Works on iPhone, Android, Google Calendar, Outlook & more
- 🆓 No API keys required
- 🛠️ Open source & free

---

## ⚙️ How It Works

1. Python script scrapes:
   https://www.wembleystadium.com/events

2. Extracts:

   - Event title
   - Date
   - Description
   - Event page link
   - Venue

3. Generates a standard `.ics` calendar file

4. GitHub Actions updates it automatically

5. GitHub Pages hosts the live subscription

Your calendar app refreshes periodically.

---

## 📱 Subscribe on iPhone / iPad

**Settings → Calendar → Accounts → Add Account → Other → Add Subscribed Calendar**

Paste:

```
https://nayshal.github.io/wembley-calendar/wembley.ics
```

Tap **Next → Save**

---

## 🤖 Subscribe on Android (Google Calendar)

Google Calendar mobile apps can’t add URLs directly.

### Use Web Method:

1. Open https://calendar.google.com
2. Click **+** next to “Other calendars”
3. Select **From URL**
4. Paste the feed URL
5. Click **Add calendar**

Syncs automatically to your phone.

---

## 💼 Subscribe in Outlook

### Outlook Web / Office 365

1. Open Calendar
2. Add calendar → Subscribe from web
3. Paste URL
4. Name it → Import

### Outlook Desktop

Add Calendar → From Internet → Paste URL

---

## 🍎 Subscribe on macOS

Calendar → File → New Calendar Subscription → Paste URL

---

## 🔄 Refresh Behavior

Subscriptions update automatically:

- Apple Calendar: every few hours to daily
- Google Calendar: ~8–24 hours
- Outlook: varies

To force refresh: remove and re‑add the subscription.

---

## 🛠️ Run Your Own Version

### Requirements

- Python 3
- requests
- beautifulsoup4
- ics

Install:

```
pip install -r requirements.txt
```

Run:

```
python generate.py
```

---

## 🤖 Automation

GitHub Actions runs on a schedule and updates the calendar file.

GitHub Pages serves the public feed.

---

## ⚠️ Limitations

- Event times not included (all‑day for consistency)
- Refresh timing controlled by calendar apps
- Venue photos may not appear for subscribed calendars
- Depends on data from official site

---

## 📜 Disclaimer

Not affiliated with Wembley Stadium.  
All data sourced from the public website.

---

## 📄 License

MIT — free to use, modify, and share.

---

<p align="center">
  Made with ❤️ for football fans & concert‑goers
</p>
