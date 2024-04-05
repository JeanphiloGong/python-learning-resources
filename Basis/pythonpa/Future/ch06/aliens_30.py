#coding=utf-8
aliens = []
for alien in range(30):
	new_alien = {'color': 'green', 'point' :5, 'speed': 'slow'}
	aliens.append(new_alien)
print("The past five aliens' element: ")
for alien in aliens[:5]:
	
	print(alien)
print("...")

print("Total number of alien: " + str(len(aliens)))
