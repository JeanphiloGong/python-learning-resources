import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Test name_function.py"""
	
	def test_first_last_name(self):
		"""Can we correctly handle names like Janis and Joplin"""
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')
	
	
	def test_first_last_middle_name(self):
		"""Can we correctly handle names like Wolfgang Amadeus Mozart"""
		formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
		
unittest.main()
