def two_pointers(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Example usage:
nums = [1, 2, 3, 4, 5]
target = 7
result = two_pointers(nums, target)
if result:
    print(result[0] + 1, result[1] + 1)  # Add 1 to indices to match 1-based indexing
else:
    print("None")