from django.urls import include, path
from rest_framework import routers
from api.views import CreateDownloadTaskView,ListPicturesView,PictureList

router = routers.DefaultRouter()
router.register(r'page_create', CreateDownloadTaskView)
router.register(r'picture_list', ListPicturesView)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('pictures',PictureList.as_view(),name='pictures')
]
