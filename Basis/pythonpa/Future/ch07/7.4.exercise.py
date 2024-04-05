#coding= UTF-8
sandwich_orders = ['Pizza tonda','pizza al taglio','Marinara']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("\nI made your " + current_sandwich  + "  sandwich.")
	
	finished_sandwiches.append(current_sandwich)
	
print("Your sandiches: \t") 
print(finished_sandwiches)

adds = ['pastrami','pastrami','pastrami']
while adds:
	current_adds = adds.pop()
	finished_sandwiches.append(current_adds)

print(finished_sandwiches)

print("The pastrami is sold out. ")
while 'pastrami' in finished_sandwiches:
     finished_sandwiches.remove('pastrami')

print("The rest of pizza: \t")     
print(finished_sandwiches)

print("If you could visit one place in the world, where would you go?")
results = {}
active = True
while active:
  name =input("Please enter your name. ")
  place = input("Please telll me the place you would like to go.  ") 
  
  results[name] = place
  
  repeat = input("Would you like to let another person respond?(yes/no)")
  if repeat == 'no':
	  active = False

for name,place in results.items():
	print(name.title() + " wanna visit " + place)

	
	
	

