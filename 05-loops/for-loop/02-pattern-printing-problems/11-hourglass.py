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

# Method 1
for i in range(9, 4, -1):
    for space in range(9-i):
        print(' ', end = '')
    for stars in range(i - 4):
        print('* ', end = '')
    print()
    
for i in range(2, 6):
    for space in range(6 - (i + 1)):
        print(' ', end = '')
    for stars in range(i):
        print('* ', end = '')
    print()