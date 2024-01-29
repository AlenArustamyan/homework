from collections import namedtuple
arajin = namedtuple('Arajin', ['x','y'])
my_arajin = arajin(x=6  , y=9)
my_arajin1 = arajin(x=0,y=3)
print("my_arajin:", my_arajin.x, my_arajin.y)
print("my_arajin1:", my_arajin1.x, my_arajin1.y)
