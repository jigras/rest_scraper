from django.shortcuts import render
from rest_framework import generics, viewsets
from api.serializers import PageSerializer, PictureSerializer, PageSerializerText
from api.models import Page, Picture
from api.tasks import download_text_images_task
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class CreateDownloadTaskView(viewsets.ModelViewSet):
    default_serializer_class = PageSerializer
    queryset = Page.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('url',)
    serializer_classes = {
        'list': PageSerializer,
        'retrieve': PageSerializerText,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        download_text_images_task.delay(obj.pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class PagePictureTaskView(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('page',)


class ListPicturesView(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()


class PictureList(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
