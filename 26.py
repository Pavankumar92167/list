def test(str_nums):
    return max(float(s.replace(",", ".")) for s in str_nums)
str_nums = ["100", "102,1", "101.1"]
print(test(str_nums))