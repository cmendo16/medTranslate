from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Favorite
from phrases.models import Phrase  
import json 

class FavoriteViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.phrase = Phrase.objects.create(text="Hello World")
        self.toggle_url = '/api/favorites/'  # Adjust if you're using a router with a prefix

    def test_toggle_add_favorite(self):
        response = self.client.post(self.toggle_url, {'phrase_id': self.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json.data['favorited'])
        self.assertEqual(Favorite.objects.count(), 1)

    def test_toggle_remove_favorite(self):
        # First, add the favorite
        Favorite.objects.create(user=self.user, phrase=self.phrase)

        response = self.client.post(self.toggle_url, {'phrase_id': self.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.json.data['favorited'])
        self.assertEqual(Favorite.objects.count(), 0)

    def test_get_favorites_list(self):
        Favorite.objects.create(user=self.user, phrase=self.phrase)

        response = self.client.get('/api/favorites/')  # Adjust if you use a different route
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json.data), 1)
        self.assertEqual(response.json.data[0]['phrase'], self.id)

    def test_unauthenticated_access_denied(self):
        self.client.logout()
        response = self.client.get('/api/favorites/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
