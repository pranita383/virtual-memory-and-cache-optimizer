# 🧠 Virtual Memory and Cache Optimization Tool

This project is a **web-based simulation tool** that demonstrates **cache optimization algorithms**—specifically the **Least Recently Used (LRU)** cache mechanism. It visualizes cache performance (hits, misses, hit ratio) and helps users understand virtual memory concepts interactively.

---

## 📌 Features

- 🔄 Simulates LRU cache behavior for a given set of memory pages
- 📈 Shows cache performance metrics:
  - Cache Hits
  - Cache Misses
  - Hit Ratio
- 🧠 Easy-to-use web interface for interactive testing
- 🗃️ Logs performance data in an SQLite database
- 💡 Educational project combining OS, DB, and web concepts

---

## 🛠️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Backend     | Python, Flask     |
| Frontend    | HTML, CSS, JavaScript |
| Database    | SQLite (for logging) |
| Cache Logic | Custom LRU Implementation |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/virtual-memory-cache-optimizer.git
cd virtual-memory-cache-optimizer
```
---
2️⃣ Install Dependencies
```bash

pip install -r requirements.txt

```
---
3️⃣ Run the Application
```bash

python run.py
```
Visit http://127.0.0.1:5000 in your browser.
---
🗂️ Project Structure
```bash
virtual-memory-cache-optimizer/
│
├── app/
│   ├── __init__.py           # Initializes Flask app
│   ├── routes.py             # API routes
│   ├── cache_manager.py      # LRU cache logic
│   ├── performance_logger.py # Performance logging (SQLite)
│   └── config.py             # Flask configuration
│
├── templates/
│   └── index.html            # Main web UI
│
├── static/
│   ├── css/style.css         # Styling
│   └── js/script.js          # JavaScript logic
│
├── run.py                    # Entry point
├── requirements.txt          # Dependencies
└── README.md                 # This file


```

---
📚 Topics Covered
Virtual Memory Concepts

Page Replacement Algorithms (LRU)

Web Development with Flask

Frontend-Backend Integration

Performance Logging with SQLite
---
