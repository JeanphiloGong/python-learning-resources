filename = 'programming.txt'
with open(filename,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creat new games.\n")
	
with open(filename,'a') as file_object0:
	file_object0.write("I also love finding meaning in large datasets.\n")
	file_object0.write("I love creating apps that cab run in a browser.\n")
