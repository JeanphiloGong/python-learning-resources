#coding = UTF-8
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)
	
	if city == "quit":
		break
		
	else:
		print("I'd love to " + city.title() + "!")
