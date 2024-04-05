#coding=utf-8
players=['charles', 'martina','michael','florence','eli']
print(players[0:3])#从列表中选取前3个元素
print(players[1:4])#从列表中选取2,3,4，个位置的元素
print(players[:3])#从列表中选取前3个元素
print(players[3:])#从列表中第三个元素一直输出到最后一个元素
#上述为切片知识

print("Here are the first three players in my team:")
for player in players[0:3]:
 print(player.title())
 
