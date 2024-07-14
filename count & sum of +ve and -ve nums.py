sum_positive = 0
count_positive = 0
sum_negative = 0
count_negative = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    
    if num == -1:
        break
    
    if num > 0:
        sum_positive += num
        count_positive += 1
    elif num < 0:
        sum_negative += num
        count_negative += 1

if count_positive > 0:
    average_positive = sum_positive / count_positive
else:
    average_positive = 0  

if count_negative > 0:
    average_negative = sum_negative / count_negative
else:
    average_negative = 0

print(f"Average of positive numbers: {average_positive}")
print(f"Average of negative numbers: {average_negative}")
