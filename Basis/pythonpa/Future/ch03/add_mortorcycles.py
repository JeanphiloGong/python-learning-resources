#coding=utf-8
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  #���б�������
motorcycles.append('ducati')
print(motorcycles)#���б�ĩβ���Ԫ��
motorcycles.insert(0,'ducati')
print(motorcycles)#���б��ض�λ�����Ԫ��
del motorcycles[0]
print(motorcycles)#����del���ɾ��Ԫ��
poped_motorcycles = motorcycles.pop()#��������pop�����������б������һ��Ԫ��ɾ�����ҽ������
print(motorcycles)
print(poped_motorcycles)
last_owned = motorcycles.pop()
print("The last motorcycles I owned was a " + last_owned.title() + ".\n")
#��������pop�������õ�����б������һ��Ԫ�ص�ֵ����е�����
first_owned = motorcycles.pop(0)#��������Ԫ�ص���Ž�Ԫ�ش��б������
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.remove('yamaha')#��������Ԫ�ص�ֵͨ��remove����ֱ�ӽ�Ԫ�ش��б���ɾ��
print(motorcycles)

motorcycles.append('yamaha')
too_expensive = 'yamaha'#����һ���µı����������г���
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive +" is too expensive for me")
