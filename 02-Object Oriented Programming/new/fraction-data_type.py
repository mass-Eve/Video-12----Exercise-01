class Fraction:
    def __init__(self, n, d):
        self.nr = n
        self.dr = d

    def __str__(self):
        return f"{self.nr}/{self.dr}"

    def __add__(self, other):
        result_nr = self.nr * other.dr + self.dr * other.nr
        result_dr = self.dr * other.dr

        return f"{result_nr}/{result_dr}"

    def __sub__(self, other):
        result_nr = self.nr * other.dr - self.dr * other.nr
        result_dr = self.dr * other.dr

        return f"{result_nr}/{result_dr}"

    def __mul__(self, other):
        result_nr = self.nr * other.nr
        result_dr = self.dr * other.dr

        return f"{result_nr}/{result_dr}"

    def __truediv__(self, other):
        result_nr = self.nr * other.dr
        result_dr = self.dr * other.nr

        return f"{result_nr}/{result_dr}"


x = Fraction(4, 5)
print(x)

y = Fraction(5, 5)
print(x)

print(x + y)
print(x - y)
print(x * y)
print(x / y)