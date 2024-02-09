from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register('producers', views.ProducerViewSet, basename="producer")
router.register('categories', views.CategoryViewSet, basename="category")
router.register('planes', views.PlaneViewSet, basename="plane")

urlpatterns = [
    path('', include(router.urls)),
]
