import unittest
from Employee import Employee

#对Employee()进行测试
class testEmployee(unittest.TestCase):
	def setUp(self):
		"""创建一个调查对象来进行测试"""
		self.test_employee = Employee('Xiao','xiao')
		self.salary = 0
		
	def test_give_default_raise(self):
		"""测试默认的年薪是否为5000"""
		self.test_employee.give_raise()
		self.assertEqual(str(5000),self.test_employee.salary)
		
	def test_give_custom_raise(self):
		"""测试进行修改后的年薪是否正确"""
		self.test_employee.give_raise(8000)
		self.assertEqual(str(8000),self.test_employee.salary)

unittest.main()
	

