# Web Scraping & MongoDB Integration Project

A Python-based application designed to scrape quotes and author profiles from [Quotes to Scrape](https://quotes.toscrape.com) and manage this data. The project supports both synchronous and asynchronous scraping workflows, persists the extracted data to local JSON files, and integrates with MongoDB for structured storage and querying through a command-line interface (CLI).

---

## Table of Contents

- [Features & Capabilities](#features--capabilities)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
  - [1. Web Scraping (JSON Generation)](#1-web-scraping-json-generation)
  - [2. MongoDB Storage & CLI Querying](#2-mongodb-storage--cli-querying)
- [License](#license)

---

## Features & Capabilities

- **Multi-Paradigm Scraping**:
  - **Synchronous Scraper (`main.py`)**: Uses `requests` and `BeautifulSoup` to scrape quotes, authors, tags, and detailed author biography pages sequentially.
  - **Asynchronous Scraper (`main_async_version.py`)**: Uses `aiohttp` and `asyncio` for faster, concurrent page fetching.
- **Local Persistence**: Saves scraped quotes and authors into formatted `qoutes.json` and `authors.json` files.
- **MongoDB Integration (`Beispiel_Mongo_DB/`)**:
  - Structured Object-Document Mapping (ODM) utilizing `mongoengine`.
  - Database connection helper (`connect.py`) connecting to MongoDB Atlas database.
  - Database seeding tool (`seeds.py`) that reads the scraped JSON files and inserts them into a MongoDB instance, resolving references between quotes and authors.
  - Interactive search command-line interface (`main.py`) inside `Beispiel_Mongo_DB` allowing queries of quotes by author name, tags, etc.

---

## Project Structure

```text
.
├── Beispiel_Mongo_DB/         # MongoDB integration examples and scripts
│   ├── config.ini             # Database credentials and configuration
│   ├── connect.py             # Establishes connection to MongoDB
│   ├── main.py                # CLI search interface for MongoDB
│   ├── models.py              # MongoEngine schemas for Authors and Quotes
│   ├── seeds.py               # Seeds the JSON data into MongoDB
│   ├── authors.json           # Cached author profiles for seeding
│   └── qoutes.json            # Cached quotes for seeding
├── main.py                    # Synchronous web scraping script
├── main_async_version.py      # Asynchronous web scraping script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## Requirements

- Python 3.8 or higher
- A running MongoDB instance (or MongoDB Atlas cluster)

---

## Installation & Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd web_scraping
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage Guide

### 1. Web Scraping (JSON Generation)

You can run either the synchronous or asynchronous version of the scraper to extract quotes and author bios and write them to `qoutes.json` and `authors.json`.

**Option A: Synchronous Scraping**
```bash
python main.py
```

**Option B: Asynchronous Scraping**
```bash
python main_async_version.py
```

Upon completion, two files will be generated in the root directory:
- `qoutes.json`: List of quotes, their authors, and associated tags.
- `authors.json`: Author biographical details (birth date, birth location, description).

---

### 2. MongoDB Storage & CLI Querying

#### Step A: Configure the Database
Create or edit `Beispiel_Mongo_DB/config.ini` and specify your MongoDB connection credentials:
```ini
[DB]
USER = your_db_user
PASS = your_db_password
DB_NAME = your_db_name
DOMAIN = your_mongodb_domain (e.g., cluster0.xxxx.mongodb.net)
```

#### Step B: Seed the Database
Navigate to the `Beispiel_Mongo_DB` directory and run `seeds.py` to populate your MongoDB instance with data from `authors.json` and `qoutes.json`:
```bash
cd Beispiel_Mongo_DB
python seeds.py
```

#### Step C: Search Quotes using CLI
Launch the interactive command-line search tool:
```bash
python main.py
```
You can search the database using the following commands:
- **Search by Author Name**: `name: <Author Name>` (e.g., `name: Albert Einstein`)
- **Search by Single Tag**: `tag: <Tag>` (e.g., `tag: life`)
- **Search by Multiple Tags**: `tags: <Tag1,Tag2>` (e.g., `tags: life,love`)
- **Exit CLI**: Type `exit`, `close`, or `stop`.

---

## License

This project is licensed under the MIT License.
