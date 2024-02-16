# Write a decorator that measures the time a function takes to execute

import time

def calculateTime(function):
    def wrapperFunction(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'{function.__name__} ran in Time : {end - start}')
        return result
    return wrapperFunction

@calculateTime
def testFunction(n):
    time.sleep(n)

testFunction(2)