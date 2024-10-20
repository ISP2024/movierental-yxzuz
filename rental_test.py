import unittest

from pricing import NewRelease, RegularPrice, ChildrenPrice
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
	# The types of movies (price_code).
	NEW_RELEASE = NewRelease()
	REGULAR = RegularPrice()
	CHILDREN = ChildrenPrice()

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two")
		self.regular_movie = Movie("Air")
		self.childrens_movie = Movie("Frozen")
		self.customer = Customer("Spencer Reid")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air")
		self.assertEqual("Air", m.get_title())

	def test_rental_price(self):
		"""Trivial test for rental price based on the movie type."""
		rental = Rental(self.new_movie, 1, RentalTest.NEW_RELEASE)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5, RentalTest.NEW_RELEASE)
		self.assertEqual(rental.get_price(), 15.0)
		# regular movie
		rental = Rental(self.regular_movie, 2, RentalTest.REGULAR)
		self.assertEqual(rental.get_price(), 2)
		rental = Rental(self.regular_movie, 4, RentalTest.REGULAR)
		self.assertEqual(rental.get_price(), 5)
		# children movie
		rental = Rental(self.childrens_movie, 3, RentalTest.CHILDREN)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 6, RentalTest.CHILDREN)
		self.assertEqual(rental.get_price(), 6)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 5, RentalTest.NEW_RELEASE)
		self.assertEqual(rental.get_rental_points(), 5)
		self.customer.add_rental(rental)

		rental = Rental(self.regular_movie, 5, RentalTest.REGULAR)
		self.assertEqual(rental.get_rental_points(), 1)
		self.customer.add_rental(rental)

		rental = Rental(self.childrens_movie, 5, RentalTest.CHILDREN)
		self.assertEqual(rental.get_rental_points(), 1)
		self.customer.add_rental(rental)

		total = sum([rental.get_rental_points() for rental in self.customer.rentals])
		self.assertEqual(total, 7)



