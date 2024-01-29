'''
                * 
              * * * 
            * * * * * 
          * * * * * * * 
        * * * * * * * * * 
          * * * * * * * 
            * * * * * 
              * * * 
                * 
'''

rows = int(input('Enter the number of rows: '))

# Upper Part
for i in range(rows):
    for space in range(rows*2 - ((i+1)*2)):
        print(' ', end = '')
    for stars in range((i*2) + 1):
        print('* ', end = '')
    print()

# Lower Part
for i in range(rows-1):
    for space in range((i+1)*2):
        print(' ', end = '')
    for stars in range(((rows-1)*2 - 1) - (i*2)):
        print('* ', end = '')
    print()