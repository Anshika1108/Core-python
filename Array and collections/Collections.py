# Namedtuple - it returns a new tuple subclass with named fields
print("* Namedtuple")

from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(x=11,y=22)
print(p.x,p.y)

print("-----------------------------------------------------------------------------------------------")

# Defaultdict - it returns a new dictionary like object with a default value type
print("* Defaultdict")

from collections import defaultdict
dict = defaultdict(int)
dict['a'] = 3
dict['c'] = 4
print(dict['a'])
print(dict['c'])

print("-----------------------------------------------------------------------------------------------")

# Counter - it is a dict subclass for counting hashable objects
print("* Counter")

from collections import Counter
c1 = Counter("Anshika")
c2 = Counter("anshika")
print(c1)
print(c2)

print("-----------------------------------------------------------------------------------------------")

# Deque - it is a list like container with fast appends and pops on both ends
print("* Deque")

from collections import deque
d = deque([1,2,3])
d.append(5)
d.appendleft(0)
print(d)

print("-----------------------------------------------------------------------------------------------")

# ChainMap - it is a dictionary like class for creating a single view of multiple mappings
print("* ChainMap")

from collections import ChainMap
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}
combined = ChainMap(dict1,dict2)
print(combined['b'])
print(combined['c'])
print(combined)

print("-----------------------------------------------------------------------------------------------")

# OrderedDict - it is a dict subclass that remembers the order entries were added
print("* OrderedDict")

from collections import OrderedDict
o = OrderedDict()
o['a'] = 1
o['b'] = 2
o['c'] = 3
print(o)