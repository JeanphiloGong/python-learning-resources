import unittest
from city_function import city_county

class NameTestCase(unittest.TestCase):
	"""test city_function.py"""
	
	def test_city_county(self):
		city_county0 = city_county('santiago','chile')
		self.assertEqual(city_county0,'santiago,chile')
		
	def test_city_country_population(self):
		"""Can we correctly handle message like santiago chile -population"""
		city_county1 = city_county('santiago','chile',1000000)
		self.assertEqual(city_county1,'santiago,chile-1000000')
		
		   
unittest.main()


	   
