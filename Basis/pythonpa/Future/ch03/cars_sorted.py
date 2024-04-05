#coding=utf-8
cars = ['bmw', 'audi', 'toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")#对列表进行临时性排序
cars.sort(reverse=True)
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
