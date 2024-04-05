#coding=utf-8
magicians = ['Aurora', 'Melody', 'Daisy', 'Soleil']
for magician in magicians:
 print(magician)           #print前面一定要存在缩进（即空几个位置）要作为for语句的下属存在
 
for magician in magicians:#将列表magicians中的元素传递到列表magician中并进行输出
	
	print(magician.title() + "," + "that was a great trick.")
	print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you,  Everyone, That was a great magic show!")
