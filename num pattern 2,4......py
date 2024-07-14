def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(2 * j, end=" ")
        print()  

rows = 3

print_pattern(rows)
