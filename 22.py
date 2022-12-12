def test(strs):
    return sum(map(ord,filter(str.isupper,strs)))
strs =  "PytHon ExerciSEs"
print(test(strs))