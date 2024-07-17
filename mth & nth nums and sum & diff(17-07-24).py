def find_nth_max_min(arr, m, n):
    sorted_arr = sorted(arr)
    
    mth_max = sorted_arr[-m]
    
    nth_min = sorted_arr[n-1]
    
    return mth_max, nth_min

arr = [16, 16, 16, 16, 16]
M = 0
N = 1

mth_max, nth_min = find_nth_max_min(arr, M, N)

total_sum = mth_max + nth_min
difference = abs(mth_max - nth_min)

print(f"{M}st Maximum Number = {mth_max}")
print(f"{N}rd Minimum Number = {nth_min}")
print(f"Sum = {total_sum}")
print(f"Difference = {difference}")
