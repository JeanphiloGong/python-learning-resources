#coding=utf-8
age = int(input("Please enter your age:"))
if age < 4:#首先Python进行询问第一个条件
    print("Your admission cost is $0")
elif age < 18:#没有满足上一个条件之后进行下一个环节
	print("Your admission cost is $5")
elif age <65:
    print("Your admission cost is $10")
elif age <1000:
    print("Your admission cost is $5")
else:
	print("Your admission cost is $0")
#该结构可以应对检查超过两个的情节
