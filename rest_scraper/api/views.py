from django.shortcuts import render
from rest_framework import generics,viewsets
from api.serializers import PageSerializer
from api.models import Page
from api.tasks import download_text_images_task
from rest_framework import status
from rest_framework.response import Response

class CreateDownloadTaskView(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        download_text_images_task.delay(obj.pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)