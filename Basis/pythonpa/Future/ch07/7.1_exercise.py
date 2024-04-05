#coding=utf-8
modle = input("What kind of car is you wanna buy: ")
print("Let me see if I can find you a " + modle)

numbers = input("How much people in here to eat:")
numbers = int(numbers)

if numbers > 8:
	print("There is no blank.")
else:
	print("There have some blank.")

number = input("Enter a number,I will tell you if it is a multiple of 10.  ")
number = int (number)
if number %10 == 0:
	print("This number " + str(number) + " is a multiple of 10")
