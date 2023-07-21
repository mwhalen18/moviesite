from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=100,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    'placeholder': 'Find a movie'
                                }
                            ), label = "")

    class Meta:
        model = Movie
        fields = ['title']