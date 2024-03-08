import math

nr = int(input("Enter the numerator: "))
dr = int(input("Enter the denominator: "))

print(f"{nr}/{dr} yields {math.remainder(nr, dr)} as remainder.")