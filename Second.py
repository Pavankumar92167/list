def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

nums = [19,19,15,5,5,5,1,2]
print(test(nums))