class Fraction:
    def __init__(self, n, d):
        self.nr = n
        self.dr = d

    # for printing 
    def __str__(self):
        return f"{self.nr}/{self.dr}"

    # to add two fractions 
    def __add__(self, *other):

        try:
            result_nr = self.nr
            result_dr = self.dr

            # iterate through every tuple of fraction numbers
            for fraction in other:
                result_nr = (result_nr * fraction.dr) + (fraction.nr * result_dr)
                result_dr = result_dr * fraction.dr

            return Fraction(result_nr, result_dr)

        except Exception as e:
            print(e)

    # to subtract two fractions
    def __sub__(self, *other):

        try:
            result_nr = self.nr
            result_dr = self.dr

            # iterate through every tuple of fraction numbers
            for fraction in other:
                result_nr = (result_nr * fraction.dr) - (fraction.nr * result_dr)
                result_dr = result_dr * fraction.dr

            return Fraction(result_nr, result_dr)

        except Exception as e:
            print(e)

    # to multiply two fractions
    def __mul__(self, *other):
        result_nr = self.nr * other.nr
        result_dr = self.dr * other.dr
        return f"{result_nr}/{result_dr}"

    # to divide two fractions
    def __truediv__(self, *other):
        result_nr = self.nr * other.dr
        result_dr = self.dr * other.nr
        return f"{result_nr}/{result_dr}"


x = Fraction(2, 3)
print(x)

y = Fraction(4, 5)
print(x)

a = Fraction(6, 7)
print(a)

b = Fraction(8, 9)
print(b)

print(x + y + a + b)
print(x - y - a - b)