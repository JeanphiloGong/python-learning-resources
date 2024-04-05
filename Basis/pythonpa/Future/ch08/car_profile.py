#coding =UTF-8
def car_profile(manufacturer,model,car_info):
	profile = {}
	profile[manufacturer]=manufacturer
	profile[model] = model
	for key,value in car_info.items():
		profile[key]=value
		return profile
car_profile('aa','bb',cc = 'dd')
print(car_profile)
                                                       
 
