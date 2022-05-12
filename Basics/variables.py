from matplotlib import use


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(z))

print("hello")


# python variables start with a letter or _
# can only contain alphanumeric
# case sensitivity is a thing


# Can declare variables in camelCase, PascalCase, snake_case

# multiple variable assignment

x, y, z = 'a', 'b', 'c'
x = y = 1


# unpacking is a thing in python
x = [1, 2]
y, z = x

print('unpacked', x, y, z)


#  cannot use '+' with numbers and string like
# print(5+ 'a')

# python has global and local variables
# You can create global variables inside a function though.

def func():
    global x
    x= "fantastic"


func()
print(x)