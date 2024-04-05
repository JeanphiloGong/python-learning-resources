#coding = UTF-8
"""A class that can be used to present cars"""
class Car():
	"""A simple attempt to simulate a car"""
	
	def __init__(self,make,model,year):
		"""Initialize the attributes that describe the car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	
	def get_descriptive_name(self):
		"""Return neat desceiptive information"""
		long_name = str(self.year) + ' ' + self.make + ' '+ self.model
		return long_name.title()
		
	
	def read_odometer(self):
		"""Print a message indicating car mileage"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	
	def update_odometer(self,mileage):
		"""Set the odometer reading to a specific value"""
		self.odometer_reading = mileage
	
	
	def update_odometer0(self,mileage):
		"""Set the odometer reading to the specified value to prevent 
		   the odometer reading from going back"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	
	def increment_odometer(self,miles):
		"""Increse the odometer reading to the sppeicified value"""
		self.odometer_reading += miles


class ElectricCar(Car):
	"""	The uniqueness of electric vehicles"""
	def __init__(self,make,model,year):
		"""Initialize the properties of the parent class"""
		super().__init__(make,model,year)
		self.battery_size = 70
		
	def describe_battery(self):
		"""Print a message describe the battery capacity"""
		print("This car has a " + str(self.battery_size) + "-kwh battery")
	

