import pizza1

pizza1.make_pizza(16,'pepperoni')
pizza1.make_pizza(12,'mushroom','green peppers','extra cheese')

from pizza1 import make_pizza as mp
mp(16,'pepperoni')
