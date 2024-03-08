'''
    * * * * *
     * * * *
      * * *
       * *
        *
'''

rows = int(input('Enter the number of rows: '))
for i in range(rows, 0, -1):
    for space in range(rows-i):
        print(' ', end = '')
    for stars in range(i):
        print('* ', end = '')
    print()