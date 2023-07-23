from django.core.management.base import BaseCommand, CommandError
from movie_feed.models import Movie

import pandas as pd
import tmdbv3api
from tmdbv3api import TMDb

class Command(BaseCommand):
    help = "Loads all data into model from letterboxd"
    

    def add_arguments(self, parser):
        parser.add_argument("file_path", nargs=1, type=str)
        parser.add_argument('api_key', nargs=1, type=str)

    def handle(self, *args, **options):
        tmdb = TMDb()
        tmdb.api_key = options['api_key'][0]

        search = tmdbv3api.Search()
        movie = tmdbv3api.Movie()

        data_path = options.get('file_path')[0]

        
        def get_cast_and_crew(id):
            res = movie.credits(response.get('id'))
            cast = res.get('cast')
            crew = res.get('crew')

            cast = ', '.join([item.get('name') for item in cast if item.get('known_for_department') == 'Acting'][0:5])

            director = ', '.join([item.get('name') for item in crew if item.get('job') == 'Director'])

            out = {
                'director': director,
                'cast': cast
            }
            return out


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
                pass
            else:
                response = response[0]
                base_path = 'https://image.tmdb.org/t/p/original'
                poster = response['poster_path']
                backdrop = response['backdrop_path']

                cast_crew = get_cast_and_crew(response.get('id'))

                m = Movie(
                    tmdb_id = response['id'],
                    title = response['title'],
                    director = cast_crew.get('director'),
                    cast = cast_crew.get('cast'),
                    release_year = response['release_date'][0:4],
                    description = response['overview'],
                    poster_path = base_path + (poster if poster else ''),
                    background_path = base_path + (backdrop if backdrop else '')
                )
                m.save()        
                self.stdout.write(
                    self.style.SUCCESS("Successfully wrote %s to Movie" % response['title'])
                )

    