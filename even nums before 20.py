def print_even_before_20(numbers):
    found_20 = False
    for num in numbers:
        if num == 20:
            found_20 = True
            break
        if num % 2 == 0:
            print(num)

numbers_list = [2, 5, 8, 10, 15, 20, 12, 16, 18, 22]
print_even_before_20(numbers_list)
