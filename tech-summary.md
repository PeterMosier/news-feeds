Below is a clean, high‑level **Markdown process overview** you can paste directly into your GitHub repo. It summarizes everything we accomplished: reliability fixes, feed correctness, Overcast compatibility, and structural improvements to both BBC and FSN update pipelines.

---

# 📰 News Feed Automation — Process Overview

This document summarizes the architectural and workflow improvements made to the **BBC World Service** and **FSN World News** automated podcast feeds. It covers scheduling, recording, XML generation, Overcast compatibility, and code‑level enhancements.

---

## 🎯 Goals

- Generate reliable, timestamped podcast episodes for BBC and FSN.
- Ensure GitHub Actions triggers consistently despite cron drift.
- Produce valid RSS/XML feeds compatible with Overcast and other podcast apps.
- Guarantee each episode is recognized as *new* and downloaded automatically.
- Maintain clean, predictable code for both update scripts.

---

## 🕒 1. Cron Scheduling Improvements

GitHub Actions cron is **not precise** and may drift or skip runs. To improve reliability:

### **BBC**
- Reduced from 24 runs/day → **4 runs/day**.
- Scheduled at evenly spaced UTC times, each at **xx:59**:
  - `23:59`, `05:59`, `11:59`, `17:59`
- This avoids queue congestion and ensures predictable recording windows.

### **FSN**
- Scheduled at **20 minutes past the hour** to avoid collisions with BBC.
- Staggered timing reduces push conflicts and drift overlap.

---

## 🎙️ 2. Recording Window Improvements

BBC recordings now:

- Start at **xx:59** (one minute before the hour).
- Record for **480 seconds (8 minutes)**.
- Capture the bulletin even if BBC delays start times.

FSN recordings already vary in length and remain unchanged.

---

## 🧩 3. RSS/XML Episode Title Updates

Both feeds now include **timestamped episode titles** inside the `<item>` block:

```
<title>BBC News Bulletin — YYYY-MM-DD HH:MM UTC</title>
<title>FSN World News — YYYY-MM-DD HH:MM UTC</title>
```

This required:

- Updating only the **episode** `<title>` (not the channel title).
- Using scoped regex to target the `<item>` block.

---

## 🔐 4. GUID and pubDate Improvements

Each episode now includes:

- A **unique GUID** based on a timestamp.
- A **RFC 2822 pubDate** (required by Overcast).

This ensures podcast apps always detect new episodes.

---

## 📦 5. Overcast Compatibility Fixes

Overcast aggressively caches enclosure URLs.  
BBC episodes were appearing **gray** (not downloaded) because:

- The enclosure URL was static.
- The MP3 file size was identical every time.

### **Fix: Cache‑busting enclosure URLs**

Both BBC and FSN now use:

```
audio/bbc-latest.mp3?ts=UNIX_TIMESTAMP
audio/fsn-latest.mp3?ts=UNIX_TIMESTAMP
```

This forces Overcast to treat each episode as new and download it automatically.

---

## 🛠️ 6. Codebase Improvements

### **BBC (`update-bbc.py`)**
- Added timestamped enclosure URL.
- Added episode‑title replacement scoped to `<item>`.
- Added missing `import re`.
- Preserved channel‑level metadata.

### **FSN (`update-fsn.py`)**
- Added timestamped enclosure URL.
- Added episode‑title replacement scoped to `<item>`.
- Preserved channel‑level metadata.
- Retained flexible GUID and pubDate logic.

Both scripts now follow a consistent structure.

---

## 📁 7. Repository Structure

```
news-feeds/
├── audio/
│   ├── bbc-latest.mp3
│   └── fsn-latest.mp3
├── feeds/
│   ├── bbc-world-news.xml
│   └── fsn-world-news.xml
├── scripts/
│   ├── update-bbc.py
│   └── update-fsn.py
└── .github/workflows/
    ├── bbc-update.yml
    └── fsn-update.yml
```

---

## 🚀 Summary

We now have:

- Reliable cron scheduling.
- Robust recording windows.
- Clean, timestamped episode metadata.
- Fully Overcast‑compatible enclosure URLs.
- Consistent Python update scripts.
- Predictable, automated feed generation.

This setup produces stable, professional‑grade podcast feeds for BBC and FSN.

