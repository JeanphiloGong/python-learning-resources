#coding = UTF-8
class Restaurant():
	def __init__(self,restaurant_name,cuisines_type):
		self.name = restaurant_name
		self.cuisines = cuisines_type
		self.number_served = 0
	
	
	def describe_restaurant(self):
		print("\nThe restaurant is called " + self.name.title() + ".")
		print("The cuisine of the restaurant including: " + self.cuisines)
			
		
	def open_restaurant(self):
		print("The restaurant is opening!")
	
	
	def number_reading(self):
		print(str(self.number_served) + " people have dined in this restaurant.")
	
	
	def set_number_served(self,number):
		if number >= self.number_served:
			self.number_served = number
			
			
	def increment_number_served(self,number):
				self.number_served += number
				

class Flavors():
	peppers =['pepper','pepperoni']
	def __init__(self,flavors = peppers):
		self.flavors0 = flavors
	
	
	def flavors_type(self):
		print("We have the following types icecream: \t" )
		for self.flavor0 in self.flavors0 :
			print( "- " + self.flavor0 )
		

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisines_type):
		super().__init__(restaurant_name,cuisines_type)
		self.flavors = Flavors()
		
	
	

restaurant = Restaurant('hall','dinna')
restaurant.number_reading()

restaurant.set_number_served(12)
restaurant.number_reading()

restaurant.increment_number_served(12)
restaurant.number_reading()

restaurant0 = IceCreamStand('hall','lunch')
restaurant0.flavors.flavors_type()





class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name 
		self.login_attempts = 0
		
	
	
	def describe_user(self):
		print("\nThe user name is: " + self.first_name.title() + self.last_name )
	
		
	def greet_user(self):
		print("Hello! " + self.first_name + self.last_name)
		
	def attempts_reading(self):
		print("\nThe attempts is " + str(self.login_attempts))
		
	
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	
	def reset_login_attempts(self):
		self.login_attempts = 0
		
		
User1 = User('li','jie')
User1.describe_user()
User1.greet_user()

user2 = User('li','hua')
user2.attempts_reading()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.attempts_reading()
user2.reset_login_attempts()
user2.attempts_reading()
