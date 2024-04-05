class Employee():
	"""存储雇员的相关信息"""
	def __init__(self,last_name,first_name):
		self.last_name = last_name
		self.first_name = first_name
		self.salary = 0
		
	def give_raise(self,give_raise = 5000):
		"""修改雇员的工资并给出提示"""
		self.salary = str(give_raise)
		print("The employee'salary is -$" + self.salary)
		
				
	def show_name(self):
		"""给出雇员的姓名"""
		fullname = self.first_name + self.last_name
		print("The employee'name is " + fullname)
		
employee0 = Employee('hua','li')
employee0.give_raise()
employee0.show_name()

