#coding = utf-8
number = input("Enter a number, and I'ii tell you it's even or odd: ")
number = int(number)

if number %2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + "is odd.")
