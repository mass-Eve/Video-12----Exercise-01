# map(key or function, iterable to the 1st parameter)

l = [6, 7, 1, 2, 3, 4]

def map_key(item):
    return item*2

print(list(map(map_key, l)))
# or
print(list(map(lambda item: item * 2, l)))