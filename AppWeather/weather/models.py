from django.db import models


class City(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(City, max_length=35)

    def __str__(self):
        return self.name
