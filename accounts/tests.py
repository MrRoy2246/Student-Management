from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from . models import User

class AccountsTests(TestCase):
    def setUp(self):
        self.client=APIClient()
        self.user_data={
            'email':'test@example.com',
            'full_name':'Test User',
            'role':'student',
            'password':'Test1234!',
            'password2':'Test1234!'
        }
    
    def test_register(self):
        response=self.client.post('/accounts/register/',self.user_data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.first().email, self.user_data['email'])
    def test_login(self):
        User.objects.create_user(
            email='test@example.com',
            full_name='Test User',
            role='student',
            password='Test1234!'
        )
        response = self.client.post('/accounts/login/', {
            'email': 'test@example.com',
            'password': 'Test1234!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

    
    def test_profile_view_authenticated(self):
        user = User.objects.create_user(
            email='test@example.com',
            full_name='Test User',
            role='student',
            password='Test1234!'
        )
        response = self.client.post('/accounts/login/', {
            'email': 'test@example.com',
            'password': 'Test1234!'
        })
        token = response.data['access']
        # print(token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        profile_response = self.client.get('/accounts/profile/')  # adjust path if needed
        self.assertEqual(profile_response.status_code, 200)