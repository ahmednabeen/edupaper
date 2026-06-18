# EdupaperHub

A Django-based web platform for discovering scholarships and academic papers worldwide. Built with Django 6.0 and Tailwind CSS.

## Features

- **Scholarship Listings** — Browse fully funded scholarships by region and country
- **Academic Papers** — Access internship, thesis, term, and project papers
- **Blog** — Guides, tips, news, and reviews for scholarship seekers
- **Admin Panel** — Manage content via Django admin interface

## Tech Stack

- Python 3 / Django 6.0
- SQLite (development)
- django-ckeditor (rich text)
- Tailwind CSS v4 (via CDN)

## Quick Start

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed sample data
python manage.py seed_data

# Start development server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.