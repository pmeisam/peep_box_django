from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Movie, TvSeries, Episode
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Define the home view
def home(request):
    movies = Movie.objects.all()
    tvSeries = TvSeries.objects.all()
    return render(request, 'home.html', {'movies': movies, 'tvSeries': tvSeries})


# Define the about view
def about(request):
    return render(request, 'about.html')


# Define the detail view
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'PeepBox/details.html', {'movie': movie})


def series_details(request, series_id):
    series = TvSeries.objects.get(id=series_id)
    return render(request, 'PeepBox/seriesDetails.html', {'series': series})


def episode_details(request, episode_name, episode_id):
    episode = Episode.objects.get(id=episode_id)
    return render(request, 'PeepBox/episodeDetails.html', {'episode': episode})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
