from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        print(f'Creating instance of {cls.__name__} with args: {args} and kwargs: {kwargs}')
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
