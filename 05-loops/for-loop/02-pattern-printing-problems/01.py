'''
*
* * 
* * *
* * * *
* * * * *
'''
rows = int(input('Enter the number of rows you want in the pattern: '))

for i in range(rows):
    for j in range(0, i+1):
        print('* ', end = '')
    print("\r")