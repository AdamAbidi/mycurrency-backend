# MyCurrency - Backend API

A Django + DRF backend for retrieving, storing, and converting currency exchange rates from multiple providers using an adapter pattern.

---

## Features

- CRUD for currencies and providers
- Toggle provider activation and set priority
- Fetch real-time and historical exchange rates
- Async loading of historical rates (via asyncio)
- Currency conversion (single + multi-target)
- Admin-friendly converter interface
- API schema via drf-spectacular (Swagger)

---

##  Setup Instructions

git clone https://github.com/AdamAbidi/mycurrency-backend.git

cd mycurrency-backend

pip install -r requirements.txt

python manage.py runserver

---

Django Admin Panel: http://localhost:8000/admin/

Converter Admin Panel: http://localhost:8000/admin/converter/

API Documentation (Swagger UI): http://localhost:8000/api/v1/docs/


In case access login is needed, credentials are (admin,admin)


The database (db.sqlite3) comes preloaded with providers, currencies, and historical exchange rates to allow immediate testing without any additional setup or data fetching.

This ensures the system is ready to use.
