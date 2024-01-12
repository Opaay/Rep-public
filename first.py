x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#le premier element commence par 0 Le premier élément a l'index 0.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#-1ait référence au dernier élément, -2 fait référence à l'avant-dernier élément, etc
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])