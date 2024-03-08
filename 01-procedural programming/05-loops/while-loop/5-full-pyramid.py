'''
            *
           * *
          * * *
         * * * *
        * * * * *
'''

rows = int(input('Enter the rows: '))

i = 1
while (i <= rows):
    j = 0
    while (j < (rows - i)):
        print(' ', end = '')
        j += 1
    k = 0
    while (k < i):
        print('* ', end = '')
        k += 1
    i += 1
    print()