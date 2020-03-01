from django.test import SimpleTestCase
from django.urls import reverse,resolve
from api.views import CreateDownloadTaskView,PictureList,ListPicturesView,PagePictureTaskView

class TestResolvingUrls(SimpleTestCase):
    """
    Testing resolving Urls
    """

    def test_picture_list_url_is_resolved(self):
        self.assertEquals(resolve('/api/v1/picture_list/').func.cls, PagePictureTaskView)

    def test_page_create_url_is_resolved(self):
        self.assertEquals(resolve('/api/v1/page_create/').func.cls, CreateDownloadTaskView)


