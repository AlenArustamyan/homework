from collections import namedtuple
arajin = namedtuple('Arajin', ['x','y'])
my_arajin = arajin(x=6  , y=9)
print(arajin.x)
print(my_arajin.y)