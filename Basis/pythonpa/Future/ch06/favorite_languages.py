#coding=utf-8
from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'Python'
favorite_languages['sarah'] = 'C'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'Python'

for name, languages in favorite_languages.items():#���ֵ��еļ�ֵ�Խ��б���
	print(name.title() + "'s favorite language is " + languages.title() + ".")

for name in favorite_languages.keys():
	print(name.title())
	
friends = ['phil', 'sarah']

for name in favorite_languages:#���ֵ��еļ����б���
	if name in friends:
		print("Hi" + name.title() + ", I see your  favorite langage is "
	          + favorite_languages[name].title() + ".")

if 'Erin' not in favorite_languages.keys():#ͨ��keys���ֵ���м���
	print("Erin, Please take our poll!")

for name in sorted(favorite_languages.keys()):#��˳����ֵ���б���
	print(name.title() + ", thank you for taking the poll!")

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):#set���Խ��غϵ�Ԫ�ؽ����غ�
	print(language.title())
	
friends1 =['nile', 'amazon','yangtze', 'jen','sarah','edward','phil']

for friend1 in friends1:
	if friend1 in favorite_languages:
		print(friend1.title() + " Thank you for taking the poll.\n")
	if friend1 not in favorite_languages:
		print(friend1.title() + " Please take our poll.\n")
	
