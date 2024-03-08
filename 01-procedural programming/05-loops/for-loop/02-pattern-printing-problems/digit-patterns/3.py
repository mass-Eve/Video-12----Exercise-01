'''
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
'''

rows = int(input('Enter the number of rows: '))
for i in range(rows):
    for j in range(i+1):
        print(f'{i+1} ', end = '')
    print()