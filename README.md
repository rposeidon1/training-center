# Training Center Student Portal

## Live Demo

[Training Center Student Portal](https://training-center-production.up.railway.app)

A full-stack Django web application for managing students, courses, and enrollments at a training center. Built with a dark, minimalist aesthetic and a professional Django + DRF architecture.

## Tech Stack

- Python 3.13 / Django 6.0
- Django REST Framework + drf-spectacular (Swagger)
- PostgreSQL
- HTMX (live search)
- Tailwind CSS v4 (CDN)
- Docker + Docker Compose
- Gunicorn

## Features

- Role-based access control (staff vs regular users)
- Student and course CRUD
- Enrollment management
- Live search with HTMX
- Pagination
- CSV export for students and courses
- REST API with Swagger UI at `/api/schema/swagger-ui/`
- Fully containerized with Docker

## Local Setup

### Without Docker

```bash
git clone https://github.com/rposeidon1/training-center.git
cd training-center
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env  # fill in your values
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### With Docker

```bash
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Visit `http://localhost:8000`