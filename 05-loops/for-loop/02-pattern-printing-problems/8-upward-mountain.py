'''
                * 
              * * * 
            * * * * * 
          * * * * * * * 
        * * * * * * * * * 
'''
rows = int(input('Enter the number of rows: '))
for i in range(rows):
    for space in range((rows*2 - 1) - (i*2)):
        print(' ', end = '')
    for stars in range((i*2) + 1):
        print('* ', end = '')
    print()