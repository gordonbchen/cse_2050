# Creating a dict.
a = {"name": "Gordon", "age": 18, "boy": True}

# Keys must be hashable.
try:
    a[[1, 2, 3]] = "hi"
except TypeError as e:
    print(e)

print(hash("name"))
print(hash("Name"))

try:
    print(hash([1, 2, 3]))
except TypeError as e:
    print(e)

# Set item.
a.__setitem__("address", "UCONN")
print(a)

# Get item.
print(a.__getitem__("name"))

# Delete item.
del a["address"]
print(a)

# Length.
print(len(a))

# Keys.
print(a.keys())

# Values.
print(a.values())

# Items.
print(a.items())
