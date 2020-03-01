from django.test import TestCase, Client
from django.urls import reverse
from api.models import Page


class TestViews(TestCase):
    """Testing ENDPOINTS"""

    def setUp(self):
        self.client = Client()

    def test_api_v1_GET(self):
        response = self.client.get('/api/v1/')
        self.assertEquals(response.status_code, 200)

    def test_page_list_create_GET(self):
        response = self.client.get('/api/v1/page_create/')
        self.assertEquals(response.status_code, 200)

    def test_picture_list_create_GET(self):
        response = self.client.get('/api/v1/picture_list/')
        self.assertEquals(response.status_code, 200)

    def test_page_create_POST(self):
        data = {
            "url": "https://www.dorotasmakuje.com/2016/11/jak-uprazyc-slonecznik/",

        }
        response = self.client.post('/api/v1/page_create/',data=data)
        self.assertEquals(response.status_code, 201)
