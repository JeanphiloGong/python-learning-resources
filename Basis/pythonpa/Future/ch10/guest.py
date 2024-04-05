print("if you are the last one, Please enter quit")
guest_name = input("Please enter your name in here: ")
	
	
	
filename = 'guest.txt'
with open(filename,'a') as file_object:
	file_object.write(str(guest_name.title()))
	file_object.write("\n")
		

