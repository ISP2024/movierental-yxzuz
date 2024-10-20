from pricing import NewRelease, RegularPrice, ChildrenPrice


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


Movie("Air", Movie.NEW_RELEASE)
# class Base:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         print(f'Creating instance of {cls.__name__} with args: {args} and kwargs: {kwargs}')
#         if not cls._instance:
#             cls._instance = super(Base, cls).__new__(cls)
#         return cls._instance
#
# class Derived(Base):
#     pass
#
# d = Derived()  # This will print the args passed
