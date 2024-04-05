filename = 'learning_python.txt'
with open(filename) as learning_object:
	lines = learning_object.readlines()
	

for line in lines:
	new_line = line.replace('Python','C')
	print(new_line)
	print(line)
