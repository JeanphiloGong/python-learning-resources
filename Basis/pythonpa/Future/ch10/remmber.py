import json
def get_stored_username():
	"""If the user name is stored,get it"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = f_obj.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def greet_user():
	"""Greet users and indicate their names"""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open(filename,'w') as f_obj:
			json.dump(username,f_obj)
			print("We'll remember you when you come back, " + username +"!")
			
			
greet_user()
