# Generated by Django 4.2.3 on 2023-07-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_feed', '0005_movie_cast_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.TextField(default='', max_length=100),
        ),
    ]
