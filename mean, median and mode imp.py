data = [2, 4, 6, 2, 8, 4, 2]

# Mean
total = sum(data)
count = len(data)
mean = total / count
print("Mean:", mean)

# Median
data.sort()
if count % 2 == 0:  
    median = (data[count // 2 - 1] + data[count // 2]) / 2
else:  
    median = data[count // 2]
print("Median:", median)

# Mode
frequency = {}
for num in data:
    frequency[num] = frequency.get(num, 0) + 1
mode = [k for k, v in frequency.items() if v == max(frequency.values())]
print("Mode:", mode)
