number = int(input("Enter your number: "))
n = 0

for i in range(1, number+1):
    if number % i == 0:
        n += 1

if n > 2:
    print("The number is composite")
else:
    print("The number is prime")
