'''
            *
          * *
        * * *
      * * * *
    * * * * *
'''

rows = int(input('Enter the number of rows: '))
for i in range(rows):
    for space in range((rows-(i+1))*2):
        print(' ', end = '')
    for stars in range(i+1):
        print('* ', end = '')
    print()