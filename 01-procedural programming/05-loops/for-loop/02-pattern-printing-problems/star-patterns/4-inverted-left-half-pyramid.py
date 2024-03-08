'''
    * * * * *
      * * * *
        * * *
          * *
            *
'''

rows = int(input('Enter the number of rows: '))
for i in range(rows, 0, -1):
    for space in range((rows-i)*2):
        print(' ', end = '')
    for star in range(i):
        print('* ', end = '')
    print()