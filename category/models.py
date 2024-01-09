from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from media.models import Media


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=250, blank=True)
    media = GenericRelation(Media)

    def __str__(self):
        return self.name
