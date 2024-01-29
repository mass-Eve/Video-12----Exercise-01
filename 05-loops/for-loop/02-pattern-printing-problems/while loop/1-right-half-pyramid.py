'''
        *
        * *
        * * *
        * * * *
        * * * * *
'''

# Method 1
rows = int(input('Enter number of rows: '))

i = 1
while (i <= rows):
    j = 0
    while (j < i):
        print('* ', end = '')
        j += 1
    print()
    i += 1
    
# -------------------------------

# Method 2

rows = int(input('Enter the number of rows: '))

i = rows
while (i >= 1):
    j = rows
    while (j >= i):
        print('* ', end = '')
        j-= 1
    print()
    i -= 1