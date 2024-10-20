from pricing import NewRelease, RegularPrice, ChildrenPrice


class Movie:
    """
    A movie available for rent.
    """
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
    
    def __str__(self):
        return self.title
