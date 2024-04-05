#coding=utf-8
foods=('pizza','falafel','carrot cake','cannoli','ice cream')
for food in foods:
 print(food)

foods[0]='spill'#Python是拒绝修改元组内的元素的
print(foods)
