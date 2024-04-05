#coding = utf-8
def make_album(singer_name,album_name,quantity=''):
	message = {'singer':singer_name,'album':album_name}
	if quantity:
		message['quantity']=quantity
	return message
	
information = make_album('Taylor Swift','Love Story',12)
print(information)
information = make_album('Billie Elilsh','Bad guy',2)
print(information)
information = make_album('Arianna Grande','Rain on me',4)
print(information)

active = True
while active:
	singer_ = input("Enter singer name:")
	if singer_ == "quit":
		break
	album_ = input("Enter album name: ")
	if album_ == "quit":
		break
	information =make_album(singer_,album_)
	print(information)
	
