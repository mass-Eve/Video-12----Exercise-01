# This function filters out values from a given condition.

# filter(key_function, iterable)

l = [6, 7, 1, 2, 3, 4]
# filters out all the numbers from list <l> which are less than 5
print(list(filter(lambda num: num < 5, l)))
    # or
def key_func(item):
    return item < 5

print(list(filter(key_func, l)))