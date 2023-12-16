# It is used to get the item being fetched by the loop along with the indexing of that value.

names = ['John', 'Dave', 'Smith']
roll = [12, 46, 23]

listt = zip(names, roll)

# for item in listt:
#     print(item)

# for index in enumerate(listt):
#     print(f'This is the index - {index[0]} and this is the content -- {index[1]}')


for index in enumerate(listt):
    print(f'''This is the index - {index[0]} and this is the content --\n\
This is name: {index[1][0]}\
 This is roll: {index[1][1]}''')