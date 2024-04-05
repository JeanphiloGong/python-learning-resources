#coding = UTF-8
def make_pizza(*toppings):
	
	print("\nMaking a pizza with the following toppings: ")
	for topping in toppings:
		print("- "  + topping)
		
make_pizza('Pepperoni')
make_pizza('mushroom','green peppers','extra cheese')





def make_pizza0(size,*toppings):
	print("\nMaking a " + str(size) + 
	      "-inch pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)
make_pizza0(16,'Pepperoni')
make_pizza0(12,'mushroom','green peppers','extra cheese')
