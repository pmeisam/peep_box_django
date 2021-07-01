from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/<int:movie_id>', views.movie_detail, name='details'),
    path('series/<int:series_id>', views.series_details, name='series_details'),
    path('<episode_name>/<int:episode_id>',
         views.episode_details, name='episode_details'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]
