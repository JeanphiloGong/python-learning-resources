#coding =UTF-8
#coding = UTF-8
def show_magicians(magician_names):
	for magician_name in magician_names:
		print("\nThe "+ magician_name +" is konwn as a mgsician.")
	
name =['Jasonlatimer','David Blaine','Liu Qian']

show_magicians(name)
print(name)


def make_great(magician_names):
	last = []	
	while magician_names:
		current_magician = magician_names.pop()
		new_magician = "The great " + current_magician
		last.append(new_magician)
	while last:
		current1 = last.pop()
		magician_names.append(current1)
	print(magician_names)
make_great(magician_names = name)


		
	
	


