import django_filters
from django import forms

from .models import Movie

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact', widget = forms.widgets.TextInput(
        attrs={
            'placeholder': 'Find a movie'
        }
    ), label = '')

    class Meta:
        model = Movie
        fields = ['title']