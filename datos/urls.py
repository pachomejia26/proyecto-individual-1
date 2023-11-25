from django.urls import path
from . import views

urlpatterns = [
    path('play-time-genre/<str:genero>/', views.PlayTimeGenre, name='play_time_genre'),
    ]