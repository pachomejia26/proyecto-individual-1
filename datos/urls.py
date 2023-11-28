from django.urls import path
from . import views

urlpatterns = [
    path('play-time-genre/<str:genero>/', views.PlayTimeGenre, name='play_time_genre'),
    path('recomendaciones/<str:id_producto>/', views.recomendacion_juego, name='recomendaciones')

    ]