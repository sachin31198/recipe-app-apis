"""
Test for the Django admin modifications
"""
from http import client
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """Tests for Django Admin."""

    def setUp(self):
        """Create user and Client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='user@example.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test1233@example.com',
            password='testpass123',
            name='Test User',
        )

    def test_users_list(self):
        """Test users are listed on the page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)