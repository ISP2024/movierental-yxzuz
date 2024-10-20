import unittest
from pricing import get_price_code_for_movie, NewRelease, RegularPrice, ChildrenPrice
from movie import Movie
from customer import Customer

class TestPriceForMovie(unittest.TestCase):

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Adventure", "Drama"])
        self.regular_movie = Movie("Jurassic World", 2015, ["Action", "Adventure", "Drama", "Sci-Fi", "Thriller"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Children"])

    def test_get_price_code_for_movie(self):
        """Test base cases."""
        self.assertEqual(get_price_code_for_movie(self.new_movie), NewRelease())
        self.assertEqual(get_price_code_for_movie(self.regular_movie), RegularPrice())
        self.assertEqual(get_price_code_for_movie(self.childrens_movie), ChildrenPrice())

    def test_children_cases(self):
        """Test all cases of children genre."""
        movie = Movie("case", 2005, ["ChilDren"])
        self.assertEqual(get_price_code_for_movie(movie), ChildrenPrice())

        movie = Movie("case", 2005, ["CHILDREN"])
        self.assertEqual(get_price_code_for_movie(movie), ChildrenPrice())

        movie = Movie("case", 2005, ["CHILDRENss"])
        self.assertEqual(get_price_code_for_movie(movie), RegularPrice())

        movie = Movie("case", 2005, ["childrens"])
        self.assertEqual(get_price_code_for_movie(movie), ChildrenPrice())

    def test_new_movie(self):
        """Test that even if it's children genre it should have new release price."""
        movie = Movie("NEW", 2024, ["Animation", "ChilDren"])
        self.assertEqual(get_price_code_for_movie(movie), NewRelease())

    def test_mixed_genres(self):
        """Test that mix genre in this case should return Children price"""
        movie = Movie("Shrek", 2001, ["Comedy", "Children"])
        self.assertEqual(get_price_code_for_movie(movie), ChildrenPrice())
