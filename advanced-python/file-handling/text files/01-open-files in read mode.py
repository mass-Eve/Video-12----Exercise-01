# Method -1

# file_object_variable = open('file-name-in-quotations', 'file-mode')
# By default - The mode is set to read only

# file1 = open('text.txt')
# data = list(file1)
# print(data)
# print('\n')
# print('In more elegant way ~')
# print('\n')
# for lines in data:
#     print(lines, end = '')

# file1.close()

# Method -2
# This method automatically closes the file as well

with open('text.txt') as file2:
    data = list(file2)
    print(data)
    print('\n')
    print('In more elegant way ~')
    print('\n')
    for lines in data:
        print(lines, end = '')