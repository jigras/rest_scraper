from django.urls import include, path
from rest_framework import routers
from api.views import CreateDownloadTaskView

router = routers.DefaultRouter()
router.register(r'page_create', CreateDownloadTaskView)

urlpatterns = [
    path('v1/', include(router.urls)),
]
