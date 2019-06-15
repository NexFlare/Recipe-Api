from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """New user is created"""
        email = "hello@world.com"
        password = "nexflare"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_invalid_email_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_user_is_superuser(self):
        email = "hello@world.com"
        password = "nexflare"
        user = get_user_model().objects.create_superuser(email, password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
