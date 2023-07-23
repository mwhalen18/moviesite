from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .filters import MovieFilter

from .models import Movie

def movie_list(request):
    f = MovieFilter(request.GET, queryset=Movie.objects.all().order_by('title'))    
    paginator = Paginator(f.qs, 25)

    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)


    context = {
        'filter': response,
        'filtered_qs_form': f
    }

    return render(request, 'movie_feed/movie_list.html', context)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }

    return render(request, 'movie_feed/movie_detail.html', context)