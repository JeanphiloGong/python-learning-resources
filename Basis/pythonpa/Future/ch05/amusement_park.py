#coding=utf-8
age = int(input("Please enter your age:"))
if age < 4:#����Python����ѯ�ʵ�һ������
    print("Your admission cost is $0")
elif age < 18:#û��������һ������֮�������һ������
	print("Your admission cost is $5")
elif age <65:
    print("Your admission cost is $10")
elif age <1000:
    print("Your admission cost is $5")
else:
	print("Your admission cost is $0")
#�ýṹ����Ӧ�Լ�鳬�����������
