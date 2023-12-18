list2 = [("a", 3), ("b", 10), ("c", 6), ("d", 5)]

def s_f(item):
    return item[1]

print(sorted(list2, key = s_f))