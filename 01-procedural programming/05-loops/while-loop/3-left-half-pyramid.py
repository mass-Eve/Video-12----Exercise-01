'''
                *
              * *
            * * *
          * * * *
        * * * * *
'''

rows = int(input('Enter the number of rows: '))

i = 1
while (i <= rows):

    # To print the spaces 
    space = (rows*2) - i*2
    j = 0
    while (j < space):
        print(' ', end = '')
        j += 1

    # To print the stars
    stars = i
    k = 0
    while (k < stars):
        print('* ', end = '')
        k += 1

    # To print new line after before the new iteration starts and incrementation
    print()
    i += 1