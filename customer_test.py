import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import NewRelease, RegularPrice, ChildrenPrice


class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""

	# The types of movies (price_code).
	NEW_RELEASE = NewRelease()
	REGULAR = RegularPrice()
	CHILDREN = ChildrenPrice()

	def setUp(self):
		"""Test fixture contains:

		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan")
		self.regular_movie = Movie("CitizenFour")
		self.childrens_movie = Movie("Frozen")

	# @unittest.skip("No convenient way to test")
	def test_billing(self):
		"""Test for total_charge of customer rental"""
		self.c.add_rental(Rental(self.new_movie, 3, CustomerTest.NEW_RELEASE))  # 9
		self.c.add_rental(Rental(self.regular_movie, 3, CustomerTest.REGULAR))  # 3.5
		self.c.add_rental(Rental(self.childrens_movie, 3, CustomerTest.CHILDREN))  # 1.5
		self.assertEqual(self.c.get_total_charge(), 14)

	def test_total_rental_points(self):
		"""Test for total rental points of customer rental."""
		self.c.add_rental(Rental(self.new_movie, 3, CustomerTest.NEW_RELEASE))
		self.c.add_rental(Rental(self.regular_movie, 3, CustomerTest.REGULAR))
		self.c.add_rental(Rental(self.childrens_movie, 3, CustomerTest.CHILDREN))
		self.assertEqual(self.c.get_total_rental_points(), 5)


	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4, CustomerTest.NEW_RELEASE)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
