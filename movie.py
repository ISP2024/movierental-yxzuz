from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days: int) -> float:
        """Straight $3 per-day charge."""
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        """New release rentals earn 1 point for each day rented."""
        frequent_renter_points = 0
        frequent_renter_points += days
        return frequent_renter_points


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days: int) -> float:
        # Two days for $2, additional days 1.50 per day.
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1


class ChildrenPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_price(self, days: int) -> float:
        # Three days for $1.50, additional days 1.50 per day.
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDREN = ChildrenPrice()
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title

    def get_price(self, days):
        """Calculate the price of movie.
        Returns:
            price of movie
        """
        return self.get_price_code().get_price(days)

    def get_rental_points(self, days):
        """Calculate rental points for movie.
        Returns:
            the frequency of renter points
        """
        return self.get_price_code().get_rental_points(days)
    
    def __str__(self):
        return self.title
