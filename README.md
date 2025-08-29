# OCA Project - Daily Scripture Reading Proof of Concept

## Overview

This project is a refactored Django-based version of the OCA daily scripture reading page on their official website.

At present, **this repository only contains the proof-of-concept (POC) for the daily scripture reading page**. It demonstrates how a user can view a single scripture reading based on the day of the year, using a CSV file as the data source.

The full project will eventually include:

- Saints and their lives
- Hymns and liturgical texts
- Icon galleries
- Integration with historical liturgical data
- Dynamic daily readings with proper Paschalion calculations

## Current Scope

- Daily scripture page (`/readings/`)
- Reads from `data/tables/scriptures.csv`
- Picks a scripture reading based on the day of the year
- Basic HTML template to display the reading

## Project Structure

```

oca\_project/
├── manage.py
├── apps/
│   └── readings/            # Current POC app
├── data/
│   └── tables/scriptures.csv
├── static/
├── templates/
└── oca\_project/             # Django project settings, URLs

```

## Setup Instructions

1. **Clone the repository** (or pull the latest if already cloned):

   ```bash
   git clone <repository_url>
   cd oca_project
   ```

````

2. **Activate your virtual environment**:

   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies** (if not already installed):

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations** (even though the POC does not yet use the database heavily):

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **View the daily reading**:

   Open your browser and go to:
   [http://127.0.0.1:8000/readings/](http://127.0.0.1:8000/readings/)

## Notes for Father John

* Currently, this is a **POC** for one page only.
* The scripture CSV (`data/tables/scriptures.csv`) is used directly. Future versions will migrate this into a database model.
* You can refresh daily and see the scripture reading for that day, automatically picked by the system.

## Future Work

* Add full migration of scripture data to a Django model
* Expand `/readings/` to include multiple readings (OT, NT, Deuterocanon) per day
* Add saints, troparia, hymns, and icons
* Implement proper Paschalion and feast day logic
* Polish front-end template for readability

---
````
