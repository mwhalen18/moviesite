from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import MovieForm

from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }

    return render(request, 'movie_feed/movie_list.html', context)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }

    return render(request, 'movie_feed/movie_detail.html', context)