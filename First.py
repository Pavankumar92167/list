def list_occurrences(l):
    return True if l.count(19) == 2 and l.count(5) >= 3 else False

print(list_occurrences([19, 15, 15, 5, 3, 3, 5, 2]))