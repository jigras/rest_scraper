from django.test import TestCase, Client
from django.urls import reverse
from api.models import Page
import json
from time import sleep

class TestAPI(TestCase):
    """Testing API"""

    def setUp(self):
        self.client = Client()
        self.page_id = 1

    def test_scraped_page(self):
        data = {
            'url': 'https://pl.wikipedia.org/wiki/Django_(framework)',
        }

        response = self.client.post('/api/v1/page_create/', data=data)
        self.assertEquals(response.status_code, 201)
        self.page_id = response.json().get('id')

    def test_custom_serializer(self):
        data = {
            'url': 'https://pl.wikipedia.org/wiki/Django_(framework)',
        }

        response = self.client.post('/api/v1/page_create/', data=data)
        self.assertEquals(response.status_code, 201)
        self.page_id = response.json().get('id')
        response = self.client.get('/api/v1/page_create/{}/?format=json'.format(self.page_id))

        assert 'text' in response.json().keys()