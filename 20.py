def test(nums):
    return "Increasing." if all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)) else \
        "Decreasing." if all(nums[i + 1] < nums[i] for i in range(len(nums) - 1)) else \
        "Not a monotonic sequence!"
nums = [1,2,3,4,5,6]
print(test(nums))