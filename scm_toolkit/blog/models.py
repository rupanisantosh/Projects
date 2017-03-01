from django.db import models
from django.contrib.sites.models import Site

# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.id,instance.id, extension)


class Post(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(upload_to=upload_location,
        null=True, blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
