#coding = UTF-8
prompt = ("Please enter your age,I'll tell you the fare.")
while True:
  price = input(prompt)
  if  price =='quit':
	  break
  price =int(price)

  if price < 3 :
    print("The fare is free")

  elif price <= 12:
    print("The fare is 10$")
  else:
    print("The fare is 15$")
