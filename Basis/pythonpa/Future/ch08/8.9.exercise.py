#coding = UTF-8
name =['Jasonlatimer','David Blaine','Liu Qian','Ma']
def show_magicians(magician_names):
	for magician_name in magician_names:
		print("\nThe "+ magician_name +" is konwn as a magsician.")
	print(magician_names)
show_magicians(name)

def make_great(magician_names):
	last = []
	person = []
	while magician_names:
		current_magician = magician_names.pop()
		new_magician = "The great " + current_magician
		last.append(new_magician)
	while last:
		current1 = last.pop()
		magician_names.append(current1)
		
	print(magician_names)
make_great(name[:])
print(name)


		
	
	

