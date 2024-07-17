def find_peak_element(nums):
    n = len(nums)
    
    if n == 1:
        return 0
    
    for i in range(n):
        if (i == 0 or nums[i] > nums[i - 1]) and (i == n - 1 or nums[i] > nums[i + 1]):
            return i
    
    return -1

nums = [1, 2, 3, 1]
peak_index = find_peak_element(nums)
print("Output:", peak_index)
