#coding=utf-8
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']#可以根据已有的键值对为新的键值对进行赋值
print("You just earned " + str(new_points) + " points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
