# multiline strings

a = """Hello darkness my old frind
Here ive come for you again

vision is slightly peaking and i can't really do anything

fuck it all I have to limit what I see in the sound of silence.

"""

# strings are arrays.
print(a[0])

count_h = 0
for l in a:
    if l == 'h':
        count_h += 1
print("numebr of h", count_h)

if "Here" in a:
    print("yea")


# slicing strings
b = "  hello, world!"

print(b[2:3])

# slice from start

print(b[:2])

# slice to end

print(b[2:])

# negative index
print(b[-5:-2])


# uppercase
print(b.upper())

# lower
print(b.lower())

# remove white space
print(b.strip())


# replace
print(b.replace('h','q'))

# split
print(b.strip().split(','))