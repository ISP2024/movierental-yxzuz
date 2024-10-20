# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer
from pricing import get_price_code_for_movie


def make_movies():
    """Some sample movies."""
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("Dune: Part Two"),
        catalog.get_movie("Jurassic World"),
        catalog.get_movie("Cinderella"),
        catalog.get_movie("Young Woman and the Sea"),
        catalog.get_movie("Bridge of Spies")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        price_code = get_price_code_for_movie(movie)  # in price_code
        customer.add_rental(Rental(movie, days, price_code))
        days = (days + 2) % 5 + 1
    print(customer.statement())
