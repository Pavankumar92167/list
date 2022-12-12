def test(strs):
    return max(strs, key=lambda x: len(set(x)))
strs = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
print(test(strs))