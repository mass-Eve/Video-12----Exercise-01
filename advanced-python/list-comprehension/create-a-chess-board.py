# A1, A2, A3, ..........., A8
# .
# .
# .
# .
# .
# .
# H1, H2, H3, ..........., H8

# Method 1
alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
nos = [i for i in range(1, 9)]

# print(f'{alphas} | {nos}')

chess_board = [[(alpha, no) for no in nos] for alpha in alphas]
# print(f'{chess_board}')

for row in chess_board:
    print(row)

# Method 2

alphas = 'ABCDEFGH'
nos = [i for i in range(1, 9)]

chess_board = [[f'{letter}{no}' for no in nos] for letter in alphas]

for row in chess_board:
    print(row)

# If we wish to invert it.

for row in chess_board[::-1]:
    print(row)

# or by this way - 
alphas = 'ABCDEFGH'[::-1]
nos = [i for i in range(1, 9)]

chess_board = [[f'{letter}{no}' for no in nos] for letter in alphas]

for row in chess_board:
    print(row)