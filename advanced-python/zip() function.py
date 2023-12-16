# It makes a tuple of 2 or more than 2 list same indexed elements

names = ['John', 'Dave', 'Smith']
roll = [12, 46, 23]

listt = zip(names, roll)

# for item in listt:
#     print(item)

for item in listt:
    print(item[0])
    print(item[1])