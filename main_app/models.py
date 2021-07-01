from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    cast = models.CharField(max_length=500)
    year = models.IntegerField(default=2021)
    genre = models.CharField(max_length=20)
    image = models.CharField(max_length=500)
    movie = models.CharField(max_length=500)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class TvSeries(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    cast = models.CharField(max_length=500)
    year = models.IntegerField(default=2021)
    genre = models.CharField(max_length=20)
    image = models.CharField(max_length=500)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class Episode(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    video_link = models.CharField(max_length=500)
    tv_series = models.ForeignKey(
        TvSeries, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"
