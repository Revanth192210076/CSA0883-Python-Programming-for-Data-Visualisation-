a = 48
b = 18

while b:
    a, b = b, a % b

gcd = a

lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
