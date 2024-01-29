'''
        * * * * * 
        * * * * 
        * * * 
        * * 
        *  
'''

rows = int(input('Enter the number of rows: '))

i = rows
while (i >= 1):
    j = i
    while (j >= 1):
        print('* ', end = '')
        j-= 1
    print()
    i -= 1