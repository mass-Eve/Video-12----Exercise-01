def function():
    '''This is the function's docstring 
It can be printed using the __doc__ method '''
    return 0

function()
print(function.__doc__)

# Another way of accesing a function's docstring
help(function)