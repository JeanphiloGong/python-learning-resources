#coding = UTF-8
def describe_pet(animal_type,pet_name):
	"""display pet information"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet(animal_type='hamster',pet_name='harry')
