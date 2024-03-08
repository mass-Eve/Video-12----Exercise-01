'''
    *
    * *
    * * *
    * * * *
    * * * * *
'''

# Method 1
print('Method 1 -')
rows = int(input('Enter the the number of rows: '))
for i in range(rows):
    for j in range(i+1):
        print("* ", end = '')
    print()
    
# Method 2
print('Method 2 -')
rows = int(input('Enter the number of rows: '))
for i in range(rows, 0, -1):
    for j in range(rows, i-1, -1):
        print("* ", end = '')
    print()