#coding = UTF-8
def make_shirt(size,logo):
	print("we are going to make a size " +size +" shirt with a " +
	       logo + " logo.")
	     
make_shirt('9','flower')
make_shirt('big',"'I love Python'")
make_shirt('midst',"'I love Python'")

def describe_city(city,country = 'China'):
	print(city.title() +" is in " + country.title())
	
describe_city('guizhou')
describe_city('paris','london')
describe_city(city = 'sichuan')
