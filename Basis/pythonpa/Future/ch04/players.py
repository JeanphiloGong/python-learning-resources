#coding=utf-8
players=['charles', 'martina','michael','florence','eli']
print(players[0:3])#���б���ѡȡǰ3��Ԫ��
print(players[1:4])#���б���ѡȡ2,3,4����λ�õ�Ԫ��
print(players[:3])#���б���ѡȡǰ3��Ԫ��
print(players[3:])#���б��е�����Ԫ��һֱ��������һ��Ԫ��
#����Ϊ��Ƭ֪ʶ

print("Here are the first three players in my team:")
for player in players[0:3]:
 print(player.title())
 
