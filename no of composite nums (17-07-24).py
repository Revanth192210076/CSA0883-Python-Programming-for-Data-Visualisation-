array = [0, 160, 180, 270, 160, 230, 210, 190, 0]

count = 0
for num in array:
    if num < 4:
        continue
        
    for i in range(2,len(array)):
        if num % i == 0:
           count += 1
           break

print("Number of Composite Numbers =", count)
