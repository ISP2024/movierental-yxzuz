from typing import Collection
from dataclasses import dataclass
import csv
import logging


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, string):
        return string.lower() in [x.lower() for x in self.genre]

    def __str__(self):
        return f'{self.title}({self.year})'


class MovieCatalog():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.movies = []
            cls._instance._load_movies()  # Load movies once
        return cls._instance

    def _load_movies(self):
        """Read csv file line by line."""
        with open('movies.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            line_num =2
            for row in reader:
                try:
                    title = row[1]
                    year = int(row[2])
                    genres = row[3].split('|')
                    movie = Movie(title=title, year=year, genre=genres)
                    self.movies.append(movie)  # Append movie to the list
                except (IndexError, ValueError):
                    logging.error(f'Line {line_num}: Unrecognized format "{",".join(row)}"')
                    continue
                line_num += 1


    def get_movie(self, title, year=None):
        """Finds the movie by title, and optionally year."""
        for movie in self.movies:
            if movie.title == title and (year is None or  movie.year == year):
                return movie
        return None
