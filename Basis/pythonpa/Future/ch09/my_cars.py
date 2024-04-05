#coding = UTF-8
from car import Car,ElectricCar
"""Import Car class in module car"""

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_bettle = Car('volkswagen','bettle',2016)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
