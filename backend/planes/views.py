from rest_framework import viewsets
import django_filters

from .models import Plane, Category, Producer
from .serializers import ProducerSerializer, CategorySerializer, PlaneSerializer


class ProducerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    lookup_field = 'slug'

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class PlaneFilter(django_filters.FilterSet):
    order_by = django_filters.OrderingFilter(
        fields=(
            ('range', 'range'),
            ('name', 'name'),
            ('cabin_height', 'cabin_height'),
            ('cabin_width', 'cabin_width'),
            ('cabin_length', 'cabin_length'),
            ('luggage_volume', 'luggage_volume'),
            ('max_persons', 'max_persons'),
        )
    )

    class Meta:
        model = Plane
        fields = {
            'name': ["contains"],
            "category__name": ["contains"],
            "producer__name": ["contains"],
            'range': ["gt", "lt"],
            "cabin_height": ["gt"],
            "cabin_width": ["gt"],
            "cabin_length": ["gt"],
            "luggage_volume": ["gt"],
            "cabin_height": ["gt"],
            "max_persons": ["gt"],
        }

class PlaneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    lookup_field = 'slug'
    filterset_class = PlaneFilter
