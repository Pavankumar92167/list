def test(nums):
    return bin(int(nums[0],2) ^ int(nums[1],2))
nums =  ["0001", "1011"]
print(test(nums))