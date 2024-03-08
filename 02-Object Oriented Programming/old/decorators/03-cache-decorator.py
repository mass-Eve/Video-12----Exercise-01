# Implement a decorator that caches the return value of a function, so that whenever it is called with the same arguments, the cached value is returned instead of re-executing the function

import time

def cacheDecorator(function):
    cacheValue = {}
    def wrapperFunction(*args):
        if (args in cacheValue):
            print("returning value from cache")
            return cacheValue[args]
        result = function(*args)
        cacheValue[args] = result
        return result
    return wrapperFunction

@cacheDecorator
def add(a, b):
    time.sleep(4)
    return a + b

print(add(4, 8))
print(add(5, 8))
print(add(4, 8))
print(add(5, 8))