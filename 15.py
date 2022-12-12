def test(words):
    return  max(words, key=len) 
strs =  ['cat', 'car', 'fear', 'center']
print(strs)
print(test(strs))