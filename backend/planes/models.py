from django.utils.text import slugify
from django.db import models



class GenerateSlugMixin(models.Model):
    slug = models.SlugField()    

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{getattr(self, 'name')} {self.pk}")
        return super().save(*args, **kwargs)
    
    class Meta:
        abstract = True


class Category(GenerateSlugMixin, models.Model):
    name = models.CharField("Name", max_length=50)
    slug = models.SlugField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["name"]

class Producer(GenerateSlugMixin, models.Model):
    name = models.CharField("Name", max_length=50)
    country = models.CharField("Country", max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["name"]

class Plane(GenerateSlugMixin, models.Model):    
    name = models.CharField("Name", max_length=50)
    image = models.ImageField("Image", upload_to="plane")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    cabin_height = models.FloatField("Cabin Height")
    cabin_width = models.FloatField("Cabin Width")
    cabin_length = models.FloatField("Cabin Length")
    luggage_volume = models.FloatField("Luggage Volume", default=0)

    max_persons = models.IntegerField("Max persons")
    range = models.IntegerField("Range")
    speed = models.IntegerField("Speed")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["name"]
