# BACK-TEST


This a simple API that has been setup to assist the


 frontend to retrieve information


from the backend about cities including the latitude and longitude,


 name,user and also be able to edit any information needed and


also create profiles that can be retrieved.


**Design**


![Back-test](images/erd.png)


 **TECH-STACK / Technologies Used**


These are the tools or packages needed to use or run the API.


1. Backend: Django, Django REST Framework


2. Database: PostgresSQL,db.Sqlite3


3. Authentication: JWT Authentication


4. Python 3.12.3


5. Django 5.1.2


6. Swagger(testing endpoints)


**Installation**


This is how the API is setup locally


**Clone the repository**


 ![git clone](https://github.com/Allano256/back-test.git)


**Navigate into the project directory**


cd back-test


**Install dependencies**


pip install -r requirements.txt


**Run migrations**


python manage.py migrate


**Start the server**


python manage.py runserver


**Enviroment Variables**


SECRET_KEY = your_secret_key


DATABASE_URL = your_database_url


**Endpoints**


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


**example**


GET /api/users/1


Authorization: Bearer your_token_here


**Response**


{

    "id": 1,
    "username": "example_user",
    "email": "user@example.com"

}



**Error handling**



| Error Code | Message      | Description                    |


| ---------- | ------------ | ------------------------------ |


| 400        | Bad Request  | Invalid parameters             |


| 401        | Unauthorized | Authentication failed          |


|            |              |                                |


| 404        | Not Found    | Resource or endpoint not found |



**Models**


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


**JWT Authentication in My Project**


In this project, I use `djangorestframework-simplejwt` to handle JWT authentication,


which allows users to securely access protected parts of the application. When users log in,


 they receive an **access token** (for accessing APIs) and a **refresh token**


  (to renew the access token as needed without logging in again).


**Implementation**


1. **Setup**: I configured SimpleJWT in `settings.py` 

   as the main authentication backend:

   ```python

   REST_FRAMEWORK = {

       "DEFAULT_AUTHENTICATION_CLASSES": (

           "rest_framework_simplejwt.authentication.JWTAuthentication",

       ),

       "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),

       "NON_FIELD_ERRORS_KEY": "errors",

   }

   ```

   **Explanation**:

   - **`DEFAULT_AUTHENTICATION_CLASSES`**: Specifies that `JWTAuthentication` (from SimpleJWT) will be used as the default authentication method. This means all API requests will expect a valid JWT token for authentication.

   - **`DEFAULT_PERMISSION_CLASSES`**: Sets `IsAuthenticated` as the default permission class. This restricts access to views so that only authenticated users (those with valid tokens) can access them unless specified otherwise in individual views.

   - **`NON_FIELD_ERRORS_KEY`**: Changes the default key for non-field-specific errors in API responses to `"errors"`, making error responses more consistent and easier to handle on the frontend.

2. **Token Settings**: I also configured the token parameters to manage token lifetimes and security:

   ```python

   SIMPLE_JWT = {

       "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),

       "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

       "ROTATE_REFRESH_TOKENS": False,

       "BLACKLIST_AFTER_ROTATION": True,

       "ALGORITHM": "HS256",

       "SIGNING_KEY": SECRET_KEY,

       "AUTH_HEADER_TYPES": ("Bearer",),

   }

   ```
   **Explanation**:

   - **`ACCESS_TOKEN_LIFETIME`**: Sets the lifespan of access tokens to 1 hour.

    After this period,

    the access token will expire, and the user will need a new one

     (via the refresh token) to remain logged in.

   - **`REFRESH_TOKEN_LIFETIME`**: Specifies that the refresh token will last for 1 day.

    Within this period, the refresh token can be used to obtain new access

     tokens without logging in again.

   - **`ROTATE_REFRESH_TOKENS`**: When `False`, the same refresh

    token is used throughout its lifespan.

    Setting it to `True` would generate a new refresh token each time it’s used.

   - **`BLACKLIST_AFTER_ROTATION`**: When `True`, any old refresh

    tokens are blacklisted after being rotated

    (when `ROTATE_REFRESH_TOKENS` is `True`). This helps prevent

     misuse of old tokens if they’re somehow compromised.

   - **`ALGORITHM`**: Defines the encryption algorithm 

   for signing the JWTs,

    with `HS256` (HMAC with SHA-256) being secure 

    and commonly used for JWT signing.

   - **`SIGNING_KEY`**: The key used to sign the tokens, 

   typically set as the `SECRET_KEY` from your Django settings

    to ensure tokens are secure and unique to your application.

   - **`AUTH_HEADER_TYPES`**: Specifies the type of

    token to be used in the `Authorization` header,

    defaulting to `"Bearer"`, so tokens are sent in headers as

     `Authorization: Bearer <token>`.

3. **Token Endpoints**: I added routes in `urls.py` to allow users

 to create, refresh, verify, and revoke tokens:

   ```python

   from rest_framework_simplejwt.views import TokenObtainPairView,

    TokenRefreshView, TokenVerifyView, TokenBlacklistView

   urlpatterns = [

     path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),

       path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

       path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),

       path('logout/', TokenBlacklistView.as_view(), name='token_revoke'),

   ]

   ```
   - **TokenObtainPairView (`jwt/create/`)**: Issues a new access and refresh token pair when a user logs in.

   - **TokenRefreshView (`jwt/refresh/`)**: Refreshes an access token using a valid refresh token.

   - **TokenVerifyView (`jwt/verify/`)**: Verifies that a provided access token is valid.

   - **TokenBlacklistView (`logout/`)**: Revokes a refresh token, blacklisting it so it cannot be used again.
4. **Securing Views**: To protect certain views, I use Django REST Framework’s

 `IsAuthenticated` permission, ensuring only authenticated

**Credits**

A special thanks to the various Youtube videos, 

Stack Overflow and all useful resources employed during the project.

**Collaborators**

A special thank you to  

jod35 Ssali Jonathan Kiggundu who offered guidance and help with

 creating the user models and authentication side of the project.

**Contributing**

You can contribute to this API by forking the repository,

 creating a branch submitting pill requests and testing requirements.
