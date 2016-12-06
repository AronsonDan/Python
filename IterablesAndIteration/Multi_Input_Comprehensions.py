# Create list from list comprehensions
l = [i*2 for i in range(10)]

print(l)
print(type(l))
print(dir(l))

# Create dictionary from dictionary comprehensions
d = {i for i in range(10)}

print(d)
print(type(d))
print(dir(d))

# Create generator from generator comprehensions
g = (i for i in range(10))

print(g)
print(type(g))
print(dir(g))

# Multiple input comprehension

di = [(x,y) for x in range(5) for y in range(10)]

print(di)
print(type(di))
print(dir(di))

# Multiple input comprehension with multiple conditions

values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]

print(values)
print(type(values))
print(dir(values))