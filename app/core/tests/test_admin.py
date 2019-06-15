from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@halfdotfull.com',
            password='pass123'
        )

        self.client.force_login(self.admin_user)
        self.normal_user = get_user_model().objects.create_user(
            email='user@halfdotfull.com',
            password='pass123',
            name='This is a test name'
        )

    def test_listed_users(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.normal_user.email)
        self.assertContains(res, self.normal_user.name)
