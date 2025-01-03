from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User


class AuthViewsTestCase(TestCase):
    def setUp(self):
        # Setup reusable variables and client
        self.client = APIClient()
        self.signup_url = reverse("signup")  # Adjust the name to match your URL configuration
        self.login_url = reverse("login")  # Adjust the name to match your URL configuration
        
        self.user_data = {
            "email": "testuser@example.com",
            "password": "strongpassword",
            "first_name": "Test",
            "last_name": "User"
        }

        self.existing_user = User.objects.create(
            email="existinguser@example.com",
            first_name="Existing",
            last_name="User",
            password="hashedpassword",  # Note: Use hashed passwords in actual tests
            is_active=True
        )
        self.existing_user.set_password("securepassword")
        self.existing_user.save()

    def test_signup_successful(self):
        """Test user signup with valid data."""
        response = self.client.post(self.signup_url, data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "User Created Successfully")
        self.assertTrue(User.objects.filter(email=self.user_data["email"]).exists())

    def test_signup_invalid_data(self):
        """Test user signup with invalid data."""
        invalid_data = {
            "email": "invalidemail",
            "password": "jgsafdj",
            "first_name": "Test",
            "last_name": "User"
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertIn("password", response.data)

    def test_login_successful(self):
        """Test user login with valid credentials."""
        data = {
            "email": "existinguser@example.com",
            "password": "securepassword"
        }
        response = self.client.post(self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("tokens", response.data)
        self.assertEqual(response.data["message"], "Login Successfull")

    def test_login_invalid_email(self):
        """Test login with an invalid email."""
        data = {
            "email": "wronguser@example.com",
            "password": "securepassword"
        }
        response = self.client.post(self.login_url, data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "Invalid email or password")

    
