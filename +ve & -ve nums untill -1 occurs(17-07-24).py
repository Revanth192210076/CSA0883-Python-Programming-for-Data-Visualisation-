positive_numbers = []
negative_numbers = []

while True:
    num = float(input("Enter a number (enter -1 to stop): "))
    
    if num == -1:
        break
    
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

if positive_numbers:
    avg_positive = sum(positive_numbers) / len(positive_numbers)
else:
    avg_positive = 0.0

if negative_numbers:
    avg_negative = sum(negative_numbers) / len(negative_numbers)
else:
    avg_negative = 0.0

print(f"Average of positive numbers: {avg_positive:.2f}")
print(f"Average of negative numbers: {avg_negative:.2f}")
