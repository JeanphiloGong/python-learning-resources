#coding = UTF-8
from random import randint

class Die():
	def __init__(self,sides = 6):
		self.sides = sides
		
	
	def roll_die(self):
		x = randint(1,6)
		self.sides = x
		print(self.sides)

dies = Die(6)
for i in range(10):
	dies.roll_die()

