# Basic tests for the API endpoints
from django.test import TestCase
from rest_framework.test import APIClient
from .models import User

class UserApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='test@example.com')

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
