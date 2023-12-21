'''
        * * * * *
        * * * *
        * * *
        * * 
        * 
'''
rows = int(input('Enter the number of rows you want in the pattern: '))

for i in range(rows, 0, -1):
    for j in range(i):
        print('* ', end = '')
    print('\r')