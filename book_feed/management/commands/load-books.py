from django.core.management.base import BaseCommand, CommandError
from book_feed.models import Book

import pandas as pd

class Command(BaseCommand):
    help = "Loads all data into Book model from csv"

    def add_arguments(self, parser):
        parser.add_argument("file_path", nargs=1, type=str)

    def handle(self, *args, **options):
        data_path = options.get('file_path')[0]

        data = pd.read_csv(data_path)
        data = data[['title', 'creators', 'publish_date', 'description', 'ean_isbn13']]
        data['cover_path'] = "https://covers.openlibrary.org/b/isbn/" + data['ean_isbn13'].astype(str) + "-M.jpg"
        data.sort_values(by = 'title', inplace=True)


        for row in data.iterrows():
            book_in = row[1]

            b = Book(
                isbn = book_in.ean_isbn13,
                title = book_in.title,
                authors = book_in.creators,
                pub_date = book_in.publish_date,
                description = book_in.description,
                cover_path = book_in.cover_path
            )
            try:
                b.save()
                self.stdout.write(
                    self.style.SUCCESS("Successfully wrote %s to Book" % book_in.title)
                )
            except Exception as exc:
                self.stdout.write(
                    self.style.ERROR("failed to write %s to Book" % book_in.title)
                )

