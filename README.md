# Django REST API Project

This project implements a Django REST API for user create_blog, get_blog, send_mail.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x recommended)
- Django (3.x recommended)
- Django REST Framework

### Installation

1. Create a virtual environment (optional but recommended):

   -> python -m venv env
   -> source env/bin/activate  

2. Install the required packages:
   
   -> pip install -r requirements.txt

3. Apply makemigrations to set up the database:

   -> python manage.py makemigrations

4. Apply migrate to set up the database:
  
   -> python manage.py migrate

5. Create a superuser:

   -> python manage.py createsuperuser

6. Run the development server:

   -> python manage.py runserver

7. Access the API endpoints at http://127.0.0.1:8000/api/.

   => API Endpoints
        -> Create Blog
                - Endpoint: /api/create_blog/
                - Method: POST
                - Description: Create a new blog.
        -> Get Blog
                - Endpoint: /api/get_blogs/
                - Method: GET
                - Description: Get all blogs.
        -> Send Mail
                - Endpoint: /api/send_mail/
                - Method: POST
                - Description: 

