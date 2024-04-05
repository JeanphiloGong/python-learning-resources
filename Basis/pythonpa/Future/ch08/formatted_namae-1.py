#coding =UTF-8
def get_formatted_name(first_name,last_name,middle_name=''):
	full_name = (first_name + " " + middle_name + " " + last_name )
	return full_name.title()
musician = get_formatted_name('jimi','hendix')
print(musician)

	
musician = get_formatted_name('john','hooker','lee')
print(musician)
