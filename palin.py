thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Pour enlever il faut préciser l'element

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Pour pop il faut mettre l'index

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)