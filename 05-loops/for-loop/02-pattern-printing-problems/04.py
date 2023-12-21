'''
                *
              * * 
            * * *
          * * * *
        * * * * * 
'''
# no of max(stars)
rows = int(input('Enter the number of rows you want in the pattern: '))
max_space = (rows - 2) + rows

for i in range(rows):
    for space in range(0, max_space - (i - 1)*2):
        print(' ', end = '')
    
    for j in range(0, i+1):
        print('* ', end = '')
    print('\r')