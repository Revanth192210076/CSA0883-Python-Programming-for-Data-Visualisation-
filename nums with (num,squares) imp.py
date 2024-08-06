start=int(input("Enter the starting:"))
end=int(input("Enter the ending:"))
 
a=[(x,x**2) for x in range(start,end+1)]
print(a)
