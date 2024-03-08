'''
        * * * * * 
         * * * *
          * * *
           * *
            * 
           * *
          * * *
         * * * *
        * * * * * 
'''

rows = int(input('Enter the number of rows: '))

for i in range((rows+1), 1, -1):
    for space in range((rows+1) - i):
        print(' ', end = '')
    for stars in range(i - 1):
        print('* ', end = '')
    print()
    
for i in range(2, (rows+1)):
    for space in range((rows+1) - (i + 1)):
        print(' ', end = '')
    for stars in range(i):
        print('* ', end = '')
    print()