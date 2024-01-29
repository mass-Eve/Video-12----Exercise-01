'''
        * * * * *
          * * * *
            * * *
              * *
                *
'''

rows = int(input('Enter the number of rows: '))

# <i> is the iterator for the main loop. It helps in iterating through every row
i = rows

# <spaces> is the iterator for the spaces loop. It helps in printing the required amount of spaces in the start of every row.
spaces = 0

while (i >= 1):
    # Iterating through the spaces loop
    j = 0
    while (j < spaces*2):
        print(' ', end = '')
        j += 1
    
    # Iterating through the stars loop
    stars = i
    while (stars >= 1):
        print('* ', end = '')
        stars -= 1

    # Decrementing the value of <i> for the main loop
    i -= 1
    # Incrementing the value of <space>
    spaces += 1
    # New line before new iteration
    print()