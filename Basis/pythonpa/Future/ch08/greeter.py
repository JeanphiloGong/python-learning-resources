#coding=utf-8
def greet_user():
	"""show simple greetings"""
	print("Hello!")

greet_user()#��ʾ���ʺ���
	
def greet_user(username):
	"""show simple greting"""
	print("Hello, " + username.title() + "!" )
	
greet_user('jesse')
