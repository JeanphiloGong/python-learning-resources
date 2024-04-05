#coding=UTF-8
def sandich(*toppings):
	print("\nMaking a sandich with the following topping: ")
	for topping in toppings:
		print("- " + topping)
sandich('pepperoni')
sandich('pepper','mushroom')
