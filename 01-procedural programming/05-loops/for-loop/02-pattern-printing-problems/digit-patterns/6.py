'''
    9 9 9 9 9
    7 7 7 7
    5 5 5
    3 3
    1
'''

rows = int(input('Enter the number of rows: '))
for row in range(rows, 0, -1):
    for column in range(row):
        print(f'{(row-1) * 2 + 1}', end = ' ')
    print()