from django.test import TestCase
from authapp.models import User
from django.test.client import Client


class UserManagementTestCase(TestCase):
    username = 'django'
    email = 'a@a.com'
    password = 'qwerty'

    new_user_data = {
        'username': 'd1',
        'first_name': 'd2',
        'last_name': 'd3',
        'password1': '12345',
        'password2': '12345',
        'email': 'r@r.ru',
        'age': '55'
    }

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            self.username,
            email=self.email,
            password=self.password
        )
        self.client = Client()

    def tearDown(self) -> None:
        pass

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/users/login/')
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

    def test_profile_redirect(self):
        response = self.client.get('/users/profile')
        print(response.status_code)
        self.assertEqual(response.status_code, 301)

