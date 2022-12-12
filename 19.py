def test(s):
    if " " in s:
        return s.split(" ")
    if "," in s:
        return s.split(",")
    return [c for c in s if c.islower() and ord(c) % 2 == 0]

strs = "a b c d"
print(strs)
print(test(strs))