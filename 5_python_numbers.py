# There are three numeric types in Python:
# int
# float
# complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

print("|----------------------|")

# int 
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


print("|----------------------|")

# float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

print("|----------------------|")

# complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print("|----------------------|")



# type convert 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("|----------------------Last|")


import random

print(random.randrange(1, 10))
