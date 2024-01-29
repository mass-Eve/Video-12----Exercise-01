'''
        *
       * *
      * * *
     * * * *
    * * * * *
'''

rows = int(input('Enter the rows: '))
for i in range(rows):
    for space in range(rows-(i+1)):
        print(' ', end = '')
    for stars in range(i+1):
        print('* ', end = '')
    print()