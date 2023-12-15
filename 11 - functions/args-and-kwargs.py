def args(*nos):
    for i in nos:
        print(i)

args(1, 2, 3)

def kwargs(**name):
    print(name)

kwargs(ankur = 12, dev = 45)