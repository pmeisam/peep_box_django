from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    cast = models.CharField(max_length=500)
    year = models.IntegerField(default=2021)
    genre = models.CharField(max_length=20)
    image = models.CharField(max_length=500)
    movie = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} // {self.description}"
