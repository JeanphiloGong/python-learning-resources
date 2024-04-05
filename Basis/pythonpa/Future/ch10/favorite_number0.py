import json 
filename = 'number.json'
with open(filename,'w') as n_obj:
	number = input("Enter a number that is your favorite: ")
	json.dump(number,n_obj)
	
	
