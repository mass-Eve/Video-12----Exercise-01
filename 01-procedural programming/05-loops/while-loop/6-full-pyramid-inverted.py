'''
    * * * * *
     * * * *
      * * *
       * *
        *
'''

# Method 1
print('Method 1')
rows = int(input('Enter the number of rows: '))

i = rows
spaces = 0
while (i >= 1):
    j = 0
    while (j < spaces):
        print(' ', end = '')
        j += 1
    stars = i
    while (stars >= 1):
        print('* ', end = '')
        stars -= 1
    i -= 1
    spaces += 1
    print()


# Method 2
print('Method 2')
rows = int(input('Enter the number of rows: '))

i = rows
while (i >= 1):
    j = 1
    while (j < rows - (i - 1)):
        print(' ', end = '')
        j += 1
    stars = i;
    while (stars >= 1):
        print('* ', end = '')
        stars -= 1
    i -= 1
    print()