#coding=UTF-8
tips = "\nPlease enter some pizza's toppings that you need."
tips +="\nToppings:(Enter 'quit' to end)   "
while True:
	message = input(tips)
	
	if message == 'quit':
	      break
	else:
	      print("We'll add " + message + " for you!")
