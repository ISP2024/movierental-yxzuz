from typing import Collection
from dataclasses import dataclass


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
