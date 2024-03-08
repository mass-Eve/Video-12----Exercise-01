'''
2
4 4
6 6 6
8 8 8 8
'''

rows = int(input('Enter the number of rows: '))
for i in range(1, rows+1):
    for j in range(i):
        print(f'{i * 2} ', end = '')
    print()