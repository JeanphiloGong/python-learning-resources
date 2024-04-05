#coding = UTF-8
class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		
		
	def describe_user():
		print("\nThe user's name is " + self.first_name.title() 
		       + self.last_name.title())
		       
	
	def greet_user():
		print("Hello " +self.first_name.title() 
		       + self.last_name.title() + " !" )
		       
		       
class Privileges():
	def __init__(self):
		privileges = ['can add post','can delete post','can ban user'] 
		self.privileges = privileges
		
	def show_privilege(self):
		print("The privileges of the admin have: \t")
		for self.privilege in self.privileges:
			print("- " + self.privilege)
		       
		       
class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges()
		
	

user1 = Admin('li','hua')
user1.privileges.show_privilege()
