'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
'''

rows = int(input('Enter the number of rows: '))
for row in range(rows):
    for column in range(row+1):
        print(f'{row*2 + 1}', end = ' ')
    print()