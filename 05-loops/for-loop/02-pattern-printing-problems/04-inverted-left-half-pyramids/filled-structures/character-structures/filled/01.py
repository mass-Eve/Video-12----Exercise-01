'''
        * * * * *
          * * * *
            * * *
              * * 
                * 
'''
rows = int(input('Enter the number of rows you want in the pattern: '))
max_space = (rows - 2) + rows

for i in range(0, rows):

    if i > 0:
        for space in range(0, i*2):
            print(' ', end ='')
        for j in range(rows - i, 0, -1):
            print('* ', end = '')
    else:
        for j in range(rows - i, 0, -1):
            print('* ', end = '')
    print('\r')