from django.test import TestCase
from api.models import Page, Picture
from django.utils.timezone import now


class TestModels(TestCase):
    """Testing models"""

    def setUp(self):
        self.page_create = Page.objects.create(url='https://www.dorotasmakuje.com/2016/11/jak-uprazyc-slonecznik/',
                                               text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                    'Sed mattis vehicula odio, ac semper nisl tincidunt vel. '
                                                    'Aliquam eget to eget eros elementum semper eu at felis. '
                                                    'Morbi ac tincidunt',
                                               scraped_at=now(),
                                               scraped=True)
        self.picture_create = Picture.objects.create(page=self.page_create,
                                                    picture='https://www.dorotasmakuje.com/resources/'
                                                            'jak_uprazyc_slonecznik.jpg')

    def test_long_text_create(self):
        self.assertEquals(self.page_create.text, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                 'Sed mattis vehicula odio, ac semper nisl tincidunt vel. '
                                                 'Aliquam eget to eget eros elementum semper eu at felis. '
                                                 'Morbi ac tincidunt')
    def test_creating_picture(self):
        self.assertEquals(self.picture_create.picture,'https://www.dorotasmakuje.com/resources/jak_uprazyc_slonecznik.jpg')