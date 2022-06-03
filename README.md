## Project: snacks-api

Containerized (Docker) Django REST API

### Author: Polo Gonzalez

### Setup

##### Django Rest Framework API

Docker container uses Python Alpine image (with bash added) to minimize weight.

#### Dependecies:

- Django
- Django REST Framework

*see requirements.txt for complete information.*

#### Run:

To run stand alone: `python manage.py runserver`
List view url:  127.0.0.1/api/v1/snacks
Detail view url:  127.0.0.1/api/v1/snacks/1

To build container and run: `docker compose up --build`
List view url:  0.0.0.0:8000/api/v1/snacks
Detail view url:  0.0.0.0:8000/api/v1/snacks/1

Use `docker compose run web bash` to add super user.

#### Tests

##### Run: python manage.py test

##### 6 unit tests

Full CRUD functionality

---

