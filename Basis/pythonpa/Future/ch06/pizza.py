#coding = utf-8
pizza = {'crust': 'thick',
         'toppings':['mushrooms','extra cheese'],}
print("You ordered a " + pizza['crust'] + "-crust pizza"
       + " with the fllowing toppings: ")
for topping in pizza['toppings']:
	print("\t" + topping)
