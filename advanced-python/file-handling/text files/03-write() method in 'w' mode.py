# 'w' method over-writes all the content that is present in a file
with open('text1.txt', 'w') as write_file:
    write_file.write("This file was created because the write method didn't found a file with similar id to write content in it ")

# also if the file do not exist in the specified location, it will create a new file with the same title