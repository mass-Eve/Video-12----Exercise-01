string = input('Enter the string: ')

length = len(string)
print(f'The length of the string | {string} | found using built-in function is {length}')

manual_length = 0
while string[manual_length:]:
    manual_length += 1

print(f'The length of the string | {string} | found manually  is {manual_length}')