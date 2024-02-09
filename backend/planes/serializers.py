from django.urls import reverse
from rest_framework import serializers

from .models import Plane, Category, Producer




class ProducerSerializer(serializers.ModelSerializer):
    self = serializers.SerializerMethodField("get_self")

    def get_self(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(reverse('producer-detail', kwargs={"slug": obj.slug}))

    class Meta:
        model = Producer
        fields = ['id', 'slug', 'name', "self"]

        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorySerializer(serializers.ModelSerializer):
    self = serializers.SerializerMethodField("get_self")

    def get_self(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(reverse('category-detail', kwargs={"slug": obj.slug}))

    class Meta:
        model = Category
        fields = ['id', 'slug', 'name', "self"]

        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class PlaneSerializer(serializers.ModelSerializer):
    self = serializers.SerializerMethodField("get_self")
    category = CategorySerializer()
    producer = ProducerSerializer()

    def get_self(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(reverse('plane-detail', kwargs={"slug": obj.slug}))

    class Meta:
        model = Plane
        fields = [
            'id',
            'slug',
            'name',
            "self",
            "image",
            "category",
            "producer",
            "cabin_height",
            "cabin_width",
            "cabin_length",
            "luggage_volume",
            "max_persons",
            "range",
            "speed"
        ]

        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }