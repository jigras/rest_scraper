from django.urls import include, path
from rest_framework import routers
from api.views import CreateDownloadTaskView,ListPicturesView,PictureList,PagePictureTaskView

router = routers.DefaultRouter()
router.register(r'page_create', CreateDownloadTaskView,basename='page_create')
router.register(r'picture_list', PagePictureTaskView, basename='picture_list')


urlpatterns = [
    path('v1/', include(router.urls),name='v1'),
    path('pictures',PictureList.as_view(),name='pictures')
]
