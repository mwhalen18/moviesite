from django.db import models

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    director = models.TextField(max_length=100, default='')
    cast = models.TextField(default='')
    release_year = models.IntegerField()
    description = models.TextField(default='')
    poster_path = models.URLField(max_length=200, default='')
    background_path = models.URLField(max_length=200, default='')
