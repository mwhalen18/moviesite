from django.core.management.base import BaseCommand, CommandError
from movie_feed.models import Movie

import pandas as pd
from tmdbv3api import TMDb, Search

class Command(BaseCommand):
    help = "Loads all data into model from letterboxd"

    def add_arguments(self, parser):
        parser.add_argument("file_path", nargs=1, type=str)
        parser.add_argument('api_key', nargs=1, type=str)

    def handle(self, *args, **options):
        tmdb = TMDb()
        tmdb.api_key = options['api_key'][0]

        search = Search()
        data_path = options.get('file_path')[0]

        data = pd.read_csv(data_path, skip_blank_lines=True, skiprows=3)

        for row in data.iterrows():
            movie_in = row[1]
            response = search.movies(params = {
                'query': movie_in.Name,
                'year': str(movie_in.Year)
            })

            if len(response) == 0:
                self.stdout.write(
                    self.style.WARNING(f"Unable to find data for {movie_in.Name} ({movie_in.Year})")
                )
            else:
                response = response[0]
                m = Movie(
                    tmdb_id = response['id'],
                    title = response['title'],
                    release_year = response['release_date'][0:4],
                    image = 'https://image.tmdb.org/t/p/original' + response['poster_path']
                )
                m.save()        
                self.stdout.write(
                    self.style.SUCCESS("Successfully wrote %s to Movie" % response['title'])
                )

    