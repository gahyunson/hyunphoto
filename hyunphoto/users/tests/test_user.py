from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth import get_user_model

User = get_user_model()

class GoogleLoginTestCase(TestCase):
    def setUp(self):
        self.login_url = reverse('user:login', args=['google'])
        self.callback_url = reverse('user:callback', args=['google'])

    @patch('social_core.backends.google.GoogleOAuth2.user_data')
    @patch('social_core.backends.google.GoogleOAuth2.do_auth')
    def test_google_login_success(self, mock_do_auth, mock_user_data):
        mock_user_data.return_value = {
            'id': '1234567890',
            'email': 'testuser@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        }

        mock_do_auth.return_value = User.objects.create_user(
            email='testuser@gmail.com',
            first_name='Test',
            last_name='User'
        )

        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 302)
        self.assertIn(self.callback_url, response.url)

        response = self.client.get(self.callback_url)
        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.wsgi_request.user.email, 'testuser@gmail.com')

    # @patch('social_core.backends.google.GoogleOAuth2.do_auth')
    # def test_google_login_failure(self, mock_do_auth):
    #     mock_do_auth.return_value = None

    #     response = self.client.get(self.login_url)

    #     self.assertEqual(response.status_code, 302)
    #     self.assertIn(self.callback_url, response.url)

    #     response = self.client.get(self.callback_url)
    #     self.assertEqual(response.status_code, 200)

    #     self.assertFalse(response.wsgi_request.user.is_authenticated)
