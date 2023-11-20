import math

a = int(input("Enter the coefficient of x^2, that is a, here: "))
b = int(input("Enter the coefficient of x, that is b, here: "))
c = int(input("Enter the value of constant c here: "))

quad = f"{a}x^2 + {b}x + {c}"
print(f"The quadratic equation is {quad}")

# find discriminant
d = (b*b - 4*a*c)

if d < 0:
    print(f"The quadratic equation {quad} has imaginary roots.")
elif d >=0:
    if d > 0:
        print("The equation has real and distinct roots.")
        root1 = ((- b) + math.sqrt(d))/(2*a)
        root1 = ((- b) - math.sqrt(d))/(2*a)
    else:
        print("The equation has real and equal roots.")
        root1 = (-b)/(2*a)
        root2 = (-b)/(2*a)
else:
    print("Check your inputs and try again...")
    
print("The roots are as follows ~ ")
print(f"{root1}")
print(f"{root2}")