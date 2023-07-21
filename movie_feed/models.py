from django.db import models

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    release_year = models.IntegerField()
    image = models.URLField(max_length=200)
