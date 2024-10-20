from pricing import get_price_code_for_movie
class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	For simplicity of this application only days_rented is recorded.
	"""

	def __init__(self, movie, days_rented):
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented

	def get_movie(self):
		return self.movie

	def get_price_code(self):
		# get the price code
		return get_price_code_for_movie(self.movie)

	def get_days_rented(self):
		return self.days_rented

	def get_price(self):
		"""Calculate the price of rental.
		Returns:
			price of rental
		"""
		return self.get_price_code().get_price(self.get_days_rented())

	def get_rental_points(self):
		"""Calculate rental points for each rental.
		Returns:
			the frequency of renter points
		"""
		return self.get_price_code().get_rental_points(self.get_days_rented())
