# we can indicate what type of values the function is intended to take
# Note -> these are only indications. they will work even if you provide any other value. they may issue an error if the intended task is not able to completed

def sum(a:int, b:int) -> int :
    '''sum the two values'''
    return a + b

x = sum(5,6)

print(x)


def sum(a:int = 9, b:int = 6) -> int :
    '''sum the two values'''
    return a + b

x = sum(5,6)

print(x)

help(sum)


def sum(a:int = 9, b:int = 6) -> int :
    '''sum the two values'''
    return a + b

x = sum('priyee', ' shri')

print(x)