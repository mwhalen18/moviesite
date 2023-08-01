import django_filters
from django import forms

from .models import Movie

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains', widget = forms.widgets.TextInput(
        attrs={
            'placeholder': 'Find a movie',
            'style': 'width: 100%',
            'class': 'form-control'
        }
    ), label = '')

    class Meta:
        model = Movie
        fields = ['title']