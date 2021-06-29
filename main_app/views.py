from django.shortcuts import render
from django.http import HttpResponse


class Movie:
    def __init__(self, name, description, cast, year, genre, image, movie):
        self.name = name
        self.description = description
        self.cast = cast
        self.year = year
        self.genre = genre
        self.image = image
        self.movie = movie


movies = [
    Movie('Ghayeghran', 'description', 'casts', '2021', 'Drama', "https://persianhive.com/wp-content/uploads/2021/06/ghayegh-ran.jpg",
          "https://videos.files.wordpress.com/6sclyjJW/ghayeghran.mp4"),
    Movie('Jonoon', 'description', 'casts', '2021', 'Drama', "https://persianhive.com/wp-content/uploads/2021/06/jonoon.jpg",
          "https://persianhive.com/01ef48c5-00fc-4b50-976b-a211bbcfdd0a"),
    Movie('Ghayeghran', 'description', 'casts', '2021', 'Drama', "https://persianhive.com/wp-content/uploads/2021/06/khamooshiye-darya.jpg",
          "https://videos.files.wordpress.com/6sclyjJW/ghayeghran.mp4")
]


# Define the home view
def home(request):
    return render(request, 'home.html', {'movies': movies})


# Define the about view
def about(request):
    return render(request, 'about.html')
