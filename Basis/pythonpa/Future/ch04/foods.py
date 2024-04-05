#coding=utf-8
my_foods = ['pizza','falafel', 'carrot cake']
friend_foods = my_foods[ : ]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite food are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

for my_food in my_foods[:]:
  print(my_food)
for friend_food in friend_foods[:]:
  print(friend_food)
