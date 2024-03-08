string = input('Enter the string you want to search in')

search_for = input('Enter the string you want to search: ')

# built-in count() working -
x = string.count(search_for)
print(f'{x}')

# manual method -

# Step 1 --> Split the string by the character whose occurences you want to search.
string_split = string.split(search_for)

# Step 2 --> The total occurences will be 1 less than the length of the string_split variable.
occurence_count = len(string_split) - 1

# Step 3 --> Print 
print(occurence_count)