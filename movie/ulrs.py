from django.urls import path
from . import views
from .models import Movie

urlpatterns = [
    path('', views.MovieListView.as_view(), name = 'movie-list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name = 'movie-detail'),
    path('add/', views.MovieCreateView.as_view(), name='movie-create'),
    path('<int:pk>/update', views.MovieUpdateView.as_view(), name='movie-update'),
    path('<int:pk>/delete', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('current/', views.CurrentMoviesListView.as_view(), name='current-movies'),
    path('upcoming/', views.UpcomingMoviesListView.as_view(), name='upcoming-movies'),
   
]
