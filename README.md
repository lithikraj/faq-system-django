# Documentation

# FAQ System - Django

## Overview
This project is a FAQ management system built using Django and Django REST Framework. It supports multilingual FAQ management and provides an API to fetch FAQs in different languages. It uses the `django-ckeditor` package for WYSIWYG editor support and stores FAQ translations in multiple languages.

## Features
- Multilingual FAQ support (English, Hindi, Bengali, etc.)
- WYSIWYG editor for FAQ answers using `django-ckeditor`
- API for fetching FAQs with language selection support
- Caching of translations using Redis
- Unit tests for model methods and API responses
- Clear, PEP8-compliant codebase

## Installation

### Prerequisites
- Python 3.8 or higher
- Redis (for caching)
- Git
- PostgreSQL (for production, optional)

### Steps to Set Up
1. Clone the repository:
   ```bash
   git clone https://github.com/lithikraj/faq-system-django.git
   cd faq-system-django

# Set up a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the dependencies
pip install -r requirements.txt

# Set up the database (PostgreSQL or SQLite):
python manage.py migrate

# Create a superuser for accessing the admin panel
python manage.py createsuperuser

# Start the development server

python manage.py runserver

# Access the application at 
http://localhost:8000/

# API Usage
# Fetch FAQs in English (default):

curl http://localhost:8000/api/faqs/

# Fetch FAQs in Hindi:

curl http://localhost:8000/api/faqs/?lang=hi

# Fetch FAQs in Bengali:

curl http://localhost:8000/api/faqs/?lang=bn

# Testing
# To run the tests for the project, use pytest:

pytest


# Contribution
-> Fork the repository.
-> Create a new branch (git checkout -b feature-name).
-> Make your changes.
-> Commit your changes (git commit -m "feat: Add new FAQ language").
-> Push to your branch (git push origin feature-name).
-> Open a pull request.

# License
# This project is licensed under the MIT License.

---

3. **Add the README to Git**:
   After adding the content above, save the file and then stage it for commit:

   ```bash
   git add README.md

