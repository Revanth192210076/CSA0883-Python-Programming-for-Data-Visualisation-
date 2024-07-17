starting=int(input("Enter the starting number:"))
ending=int(input("Enter the ending number:"))

a=[(x,x**2) for x in range(starting,ending+1)]

print(a)
