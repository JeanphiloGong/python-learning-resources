#coding=utf-8
river_messages ={'nile':'egypt',
	             'Amazon River':'America',
	             'the Yangtze River':'China',
	             }
for river,country in river_messages.items():
	print("The " + river.title() + " runs through " + country.title())
	
					 
for river in river_messages:
	print(river)
	
for country in river_messages.values():
	print(country)
