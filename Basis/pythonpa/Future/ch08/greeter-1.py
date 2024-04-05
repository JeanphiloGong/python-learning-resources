#coding=utf-8
def get_formatted_name(first_name,last_name):
	"""Return clean name"""
	full_name = first_name + " " + last_name
	return full_name.title()
	
active = True
while active:#这是一个无限循环
	print("\nPlease tell me your name: ")
	f_name = input("First name: ")
	if f_name == 'quit':
		break
	l_name = input("Lasst_name: ")
	if l_name == 'quit':
		break
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")
 
