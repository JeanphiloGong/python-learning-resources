from name_function import *
print("Enter 'q' to quit in any time. ")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break
		
	formatted_name = get_formatted_name(first,last)
	print("\tNeatly formatted name: " + formatted_name + ".")
