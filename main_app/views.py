from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Movie


# Define the home view
def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


# Define the about view
def about(request):
    return render(request, 'about.html')


# Define the detail view
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'Details/details.html', {'movie': movie})
