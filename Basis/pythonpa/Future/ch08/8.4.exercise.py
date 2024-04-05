#coding = utf-8
def city_country(city,country):
	full_modle = city + "," +country
	return full_modle
	
while True:
	c_modle = input("\nCity:")
	if c_modle == 'quit':
		break
	co_modle = input("\ncountry: ")
	if co_modle == 'quit':
		break
	last_city_country = city_country(c_modle,co_modle)
	print(last_city_country)

