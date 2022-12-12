def test(string):
    import re
    merged = re.split(r"([ ,]+)", string)
    return [merged[::2], merged[1::2]]
s = "W3resource Python, Exercises."
print(test(s))