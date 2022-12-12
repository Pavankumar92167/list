def test(strs):
    return [len(s.split(" ")[-1])==1 for s in strs]
strs =  ['cat', 'car', 'fear', 'center']
print(test(strs))