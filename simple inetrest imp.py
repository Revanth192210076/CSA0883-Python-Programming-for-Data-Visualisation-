p=int(input("entertheprincipleamount:"))
r=int(input("enter the rate:"))
t=int(input("enter the time:"))

simple=float(p*(r/100)*t)
compound=round((p*(1+r/100)**t)-p)

print("simple:",simple)
print("compound:",compound)
