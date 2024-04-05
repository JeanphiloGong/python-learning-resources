#coding=utf-8

Peppa = {
              'kind':'pig',
			  'name':'peppa',
			  'owner':'none',
			}
Teddy = {
              'kind':'bear',
			  'name':'teddy',
			  'owner':'Mr.bean',
			 }
			 
pets = [Peppa,Teddy]
for pet in pets:
	print("Pet " + pet['name'].title() +" message: ")
	
	print(pet)
#6-8


favorite_places = {
                     'JianJan':['Manado','Ocean'],
                     'Jiessie':['Vienna','Love'],
                     'William':['Nottingham Hill','Love'],
                   }
for name,places in favorite_places.items():
	print(name.title() + " favorite places :  " )
	print(places)
#6-9


cities = { 
           'London' : {
                        'country':'British',
						'population':'9.54 million',
						'fact':"The world's largest financial center",
					  },
           'New York' : {
                        'country':'American',
						'population':'10 million',
						'fact':'One of the three largest financial centers in the world',
					  },
           'Paris' : {
                        'country':'French',
						'population':'2.24 million',
						'fact':'One of the five international metropolises in the world',
					  },
		}		  
for cities_name,message in cities.items():
	print(cities_name.title() + "'s mssage:")
	print(message)          
                      
                     
                  
