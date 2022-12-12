def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

str11 = ["a","abb","sfs", "oo", "de", "sfde"]
print(test(str11))