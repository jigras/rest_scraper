from django.shortcuts import render
from rest_framework import generics,viewsets
from api.serializers import PageSerializer,PictureSerializer
from api.models import Page,Picture
from api.tasks import download_text_images_task
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class CreateDownloadTaskView(viewsets.ModelViewSet):

    serializer_class = PageSerializer
    queryset = Page.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('url',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        download_text_images_task.delay(obj.pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ListPicturesView(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()


class PictureList(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer