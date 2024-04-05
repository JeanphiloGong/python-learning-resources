def city_county(city,county,population =''):
	"""Returns a string of cities and countries"""
	if population:
		string = city + "," + county + "-" + str(population)
	else:
		string = city + "," + county
	return string
