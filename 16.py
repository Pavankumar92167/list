def test(strs, substr):
    return [s for s in strs if substr in s]
strs =  ['cat', 'car', 'fear', 'center']
print(strs)
substrs = 'ca'
print("Substring: "+substrs)
print(test(strs, substrs))