from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Movie
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Movie

class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movie/movie_form.html'
    fields = ['title', 'director', 'release_date', 'description']
    success_url = reverse_lazy('movie-list')

class CurrentMoviewListView(ListView):
    model = Movie
    template_name = 'movie/current_moviews.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(realease_date__lte=timezone.now())
    
class UpcomingMoviewListView(ListView):
    model = Movie
    template_name = 'movie/upcoming_movies.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(release_date__gt=timezone.now())
    