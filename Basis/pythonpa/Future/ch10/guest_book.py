guests = []
while True:
	guestname = input("Enter your name: ")
	print("Hello! " + guestname.title() )
	guests.append(guestname)
	question = input("Enter 'q' or 'c' to quit or continue: ")
	if question == 'q':
		break
	else:
		continue
print(guests)
filename = 'guest_book.txt'
with open(filename,'a') as file_object:
	for guest in guests:
		print(guest)
		file_object.write(guest.title() + " has been successfully accessed "
	 + "and registered.\n")

		
	
