def test(nums):
    return [max(nums[:i]) for i in range(1, len(nums) + 1)]
nums = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
print(test(nums))