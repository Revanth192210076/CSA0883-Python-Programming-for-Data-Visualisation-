import math

def find_perfect_squares(start, end):
    perfect_squares = []
    
    for num in range(start, end + 1):

        root = math.isqrt(num)

        if root * root == num:
            perfect_squares.append(num)
    
    return perfect_squares


start_range = 1
end_range = 1000

result = find_perfect_squares(start_range, end_range)
print(result)





lower_limit = int(input("Enter the lower range: "))
upper_limit = int(input("Enter the upper range: "))

my_list = []
my_list = [x for x in range(lower_limit,upper_limit+1)
           if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]

print("The result is : ")
print(my_list)
