# LAB - Class 31

## Project: snacks-api

Containerized (Docker) small Django RESTful API

### Author: Polo Gonzalez

### Setup
Run in container or stand alone.

Container image uses Python Alpine (with bash added) to minimize weight.

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

##### Passes all 6 unit tests

Full CRUD functionality

---

