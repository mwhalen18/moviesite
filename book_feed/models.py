from django.db import models

class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    authors = models.TextField(default='')
    pub_date = models.CharField(max_length=10)
    description = models.TextField(default='')
    cover_path = models.URLField(max_length=200, default='')