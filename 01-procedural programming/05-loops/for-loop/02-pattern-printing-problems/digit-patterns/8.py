'''
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1 
    1
'''

rows = int(input('Enter the number of rows: '))
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(f'{j}', end = ' ')
    print()