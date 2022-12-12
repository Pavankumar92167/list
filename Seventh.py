def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])
nums = [0,1,2,3,4,5]
print(test(nums))