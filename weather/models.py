from django.db import models
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=35)
    url = models.SlugField(max_length=130)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(City, self).save(*args, **kwargs)


class About(models.Model):
    name = models.CharField(City, max_length=35)

    def __str__(self):
        return self.name
