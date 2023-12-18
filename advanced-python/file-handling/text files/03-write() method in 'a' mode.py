# 'a' method adds content in the end of the file and do not over-writes the previous content that is present in the file.
with open('text.txt', 'a') as write_file:
    write_file.write('\nWrite this content in the file')