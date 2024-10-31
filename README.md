# BACK-TEST

This a simple API that has been setup to assist the frontend to retrieve information from the backend about cities including the latitude and longitude, city name,user and also be able to edit any information needed adn also create profiles that can be retrieved.

# TECH-STACK

<ul>
<li> <strong>Backend: Django, Django REST Framework</strong></li>
<li> <strong>Database: PostgresSQL</strong></li>
<li> <strong>Auth: Simple JWT</strong></li>
</ul>

# Getting Started

# Prerequisites

These are the tools or packages needed to use or run the API.

<ul>
<li>Python 3.12.3 </li>
<li>Django 5.1.2 </li>
<li>Swagger(testing endpoints) </li>
</ul>

# Installation

This is how the API is setup locally

# Clone the repository

git clone https://github.com/Allano256/back-test.git

# Navigate into the project directory

cd back-test

# Install dependencies

pip install -r requirements.txt

# Run migrations

python manage.py migrate

# Start the server

python manage.py runserver

# Enviroment Variables

SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url

# Endpoints

| Method | Endpoint                  | Description            |
| ------ | ------------------------- | ---------------------- |
| GET    | /api/v1/auth              |                        |
| POST   | /api/v1/auth/jwt/create/  | Creates a city         |
| POST   | /api/v1/auth/jwt/refresh/ | refreshes token        |
| POST   | /api/v1/auth/jwt/verify/  | Verifies user          |
| POST   | /api/v1/auth/jwt/login/   | Logs in a user         |
| POST   | /api/v1/auth/jwt/logout/  | Logs out a user        |
| POST   | /api/v1/auth/jwt/signup/  | Signsup a user         |
| GET    | /api/v1/auth/{id}/        | Gets user by id        |
| PUT    | /api/v1/auth/{id}/        | Updates user by id     |
| DELETE | /api/v1/auth/{id}/        | Deletes user by id     |
| GET    | api/v1/cities             | Retrieves all cities   |
| POST   | api/v1/cities             |                        |
| GET    | /api/v1/auth/{id}/        | Retrieves a city by id |
| PUT    | /api/v1/auth/{id}/        | updates a city by id   |
| DELETE | /api/v1/auth/{id}/        | Deletes a city by id   |

# example

GET /api/users/1
Authorization: Bearer your_token_here

# Response

{
"id": 1,
"username": "example_user",
"email": "user@example.com"
}

# Error handling

| Error Code | Message      | Description                    |
| ---------- | ------------ | ------------------------------ |
| 400        | Bad Request  | Invalid parameters             |
| 401        | Unauthorized | Authentication failed          |
|            |              |                                |
| 404        | Not Found    | Resource or endpoint not found |

# Models

We have the following user model.

| Field       | Type          | Description        |
| ----------- | ------------- | ------------------ |
| first_name  | Charfield     | first name of user |
| last_name   | Charfield     | last name of user  |
| email       | EmailField    | User email         |
| is_staff    | BooleanField  | User is staff      |
| is_active   | BooleanField  | User is active     |
| date_joined | DateTimeField | Date joined        |

We have the following city model.

| Field     | Type       | Description      |
| --------- | ---------- | ---------------- |
| user      | Foreignkey | Foreignkey       |
| city_name | Charfield  | Name of city     |
| date      | DateField  | Date             |
| notes     | TextField  | Notes about city |
| lng       | FloatField | Longitude        |
| lat       | FloatField | Latitude         |

# Collaborators

A special thank you to  
jod35 Ssali Jonathan Kiggundu who offered help with creating the user models and authentication side of the project.

# Contributing

You can contribute to this API by forking the repository, creating a branch submitting pill requests and testing requirements.
