# CURD-Project-in-Django
Django CRUD Operations Project

roject Overview
This is a Django-based web application that demonstrates Create, Read, Update, and Delete (CRUD) operations. The project serves as a foundation for building database-driven web applications with Django's powerful ORM and templating system.

Features
User-friendly interface for managing data

Full CRUD functionality:

Create new records

Read/View existing records

Update existing records

Delete records

Responsive design that works on desktop and mobile devices

Form validation to ensure data integrity

Search functionality to easily find records

Pagination for large datasets

Technologies Used
Backend: Django 4.2 (Python)

Frontend: HTML5, CSS3, Bootstrap 5

Database: SQLite (default, can be configured for PostgreSQL/MySQL)

Installation Guide
Prerequisites
Python 3.8+

pip (Python package installer)

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Access the application:

Open your browser and go to http://127.0.0.1:8000/

Admin interface: http://127.0.0.1:8000/admin/

Usage Instructions
Access the main page to view all existing records

Click "Add New" to create a new record

Click on a record to view its details

Click "Edit" on a record to update its information

Click "Delete" to remove a record (with confirmation)

