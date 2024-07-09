import math

def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def is_tech(n):
    count = count_digits(n)

    
    if count % 2 != 0:
        return False

    half = count // 2
    first_half = n // 10 ** half
    second_half = n % (10 ** half)
    sum_val = first_half + second_half

    if sum_val ** 2 == n:
        return True
    else:
        return False
    

if is_tech(2025):
    print("True")
else:
    print("False")
