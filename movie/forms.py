from django.forms import ModelForm
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_date', 'description']

    title = forms.CharField(label='Movie Title', max_length=100, help_text='Enter the movie title.')
    director = forms.CharField(max_length=100, help_text='Enter the director\'s name.')
    release_date = forms.DateField(help_text='Enter the release date of the movie.')
    description = forms.CharField(widget=forms.Textarea, help_text='Enter a description for the movie.')