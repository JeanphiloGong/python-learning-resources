import json
filename = 'number.json'
with open(filename) as n_obj:
	 numbers = json.load(n_obj)
	 print("I konw your favorite number! It's " + numbers )
	 
	
