#coding = UTF-8
def greet_users(names):
	"""Issue simple questions to each user in the list"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames =['hannah','ty','margot']
greet_users(usernames)
