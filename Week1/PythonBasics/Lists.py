friends = ["Kevin","Karen","Jim"]

print(friends)

print(friends[0]+" is cool")
print("but "+friends[-1]+" is not")

print(friends[1:])

friends[1]="mike"
print(friends)
friends.append("Shrey")
print(friends)
friends.insert(1,"Roger")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop()
friends.pop()
print(friends)
print(friends.count("Kevin"))
print(friends.index("Kevin"))
print(friends)
friends2=friends.copy()
print(friends2)
# friends.clear()
# print(friends)