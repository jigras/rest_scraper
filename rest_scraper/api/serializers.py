from rest_framework import serializers
from api.models import Page,Picture

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['url','scraped','id']

class PageSerializerText(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['url','scraped','id','text']


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['picture','page']

class PageCrawled(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['url','scraped']