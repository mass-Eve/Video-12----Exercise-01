'''
    1
    2 1 
    3 2 1
    4 3 2 1
    5 4 3 2 1
'''

rows = int(input('Enter the number of rows: '))
for i in range(rows):
    for j in range(i+1, 0, -1):
        print(f'{j}', end = ' ')
    print()