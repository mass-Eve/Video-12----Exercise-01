# Create a decorator to print the function name and the values of its arguments everytime the function is called

def debug(function):
    def wrapperFunction(*args, **kwargs):
        allArgs = ', '.join( str(i) for i in args )
        allKArgs = ', '.join( f'{key} : {value}' for key, value in kwargs.items() )
        runfunction = function(*args, **kwargs)
        print(f'Function Name : {function.__name__}')
        print(f'All args : {allArgs}')
        print(f'All kwargs : {allKArgs}')

        return runfunction
    return wrapperFunction

@debug
def greet(name, greeting= 'Hello'):
    print(f'{greeting} {name}')

greet('naman')