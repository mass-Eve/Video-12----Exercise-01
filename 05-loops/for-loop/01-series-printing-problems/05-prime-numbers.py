# A program to print all the prime numbers between a given range

n1 = int(input('Enter the starting range: '))
n2 = int(input('Enter the ending range: '))

print(f'The prime numbers between [{n1}, {n2}], (both inclusive) are : ', end = '')
for i in range(n1, n2):
    count = 0
    for j in range(2, (i//2 + 1)):
        if (i % j == 0):
            count += 1
            break
    if (count == 0):
        print(f'{i}, ', end = '')