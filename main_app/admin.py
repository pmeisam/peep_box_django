from django.contrib import admin
from .models import Movie, TvSeries, Episode

# Register your models here
admin.site.register(Movie)
admin.site.register(TvSeries)
admin.site.register(Episode)