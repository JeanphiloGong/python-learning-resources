filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
	
print(pi_string)
print(len(pi_string))


birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the digits of pi!")
else:
	print("Your birthday does appear in the digits of pi.")
