from django.contrib import admin

from .models import Plane, Category, Producer

admin.site.register(Plane)
admin.site.register(Category)
admin.site.register(Producer)