"""
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
"""

start = int(input('Enter the starting number in every row of the pattern: '))
end = int(input('Enter the maximum number that has to be printed in the last row: '))

for i in  range(start, end+1):
    for j in range(start, i+1):
        print(j, end = ' ')
    print()