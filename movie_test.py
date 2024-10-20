import unittest
from customer import Customer
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Movie class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 1998, ["Animation"])
        self.regular_movie = Movie("CitizenFour", 2014, ["Documentary"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation"])

    def test_is_genre(self):
        """Test for is_genre method that it can test with any str cases."""
        self.assertFalse(self.new_movie.is_genre("Anime"))
        self.assertTrue(self.new_movie.is_genre("AnimaTiON"))
        self.assertTrue(self.regular_movie.is_genre("DOCUMENTARY"))

    def test_str(self):
        self.assertEqual(str(self.new_movie), "Mulan(1998)")
        self.assertNotEqual(str(self.regular_movie), "CitizenFour(1999)")
        self.assertNotEqual(str(self.childrens_movie), "FroZen(2013)")

