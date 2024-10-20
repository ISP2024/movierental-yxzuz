# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from pricing import NewRelease, RegularPrice, ChildrenPrice

# The types of movies (price_code).
NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrenPrice()

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air"),
        Movie("Oppenheimer"),
        Movie("Frozen"),
        Movie("Bitconned"),
        Movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    movie_price_codes = [NEW_RELEASE, REGULAR, CHILDREN, NEW_RELEASE, REGULAR]
    days = 1
    for movie, price_code in zip(make_movies(), movie_price_codes):
        customer.add_rental(Rental(movie, days, price_code))
        days = (days + 2) % 5 + 1
    print(customer.statement())
