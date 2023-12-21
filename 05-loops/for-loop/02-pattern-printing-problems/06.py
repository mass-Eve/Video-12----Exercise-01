'''
        5
        5 4
        5 4 3
        5 4 3 2
        5 4 3 2 1
'''
count = 0
for i in range(5, 0, -1):
    for j in range(5, 5 - (count + 1), -1):
        print(j, end = ' ')
    count += 1
    print()