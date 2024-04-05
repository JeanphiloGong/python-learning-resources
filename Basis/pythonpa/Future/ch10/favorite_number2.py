import json
filename = 'number.json'

try:
	with open(filename) as n_obj:
		number = json.load(n_obj)
except FileNotFoundError:
	number = input("Enter a number thai is your favorite" )
	with open(filename) as n_obj:
		json.dump(number,n_obj)
else:
	print("I know your favorite number is: " + number +"!")
