* math module in python is a library that contains a set of functions that helps the programmers in performing various mathemical tasks.

* To use math library we first have to include it in our program and for that we use "import" keyword.

        import math

* To use a function or a method present in a library, we write it in this way -

        <module-name>.<method-name>(<argument>)

Some math module functions that are most widely used are -~

01. Square-root Method : It enables us to find the square root of a number.
Syntax

        math.sqrt(<value>)


02. Ceil Method : This method rounds UP number a to the nearest integer, if necessary, and returns the result.
Syntax

        math.ceil(<value>)


03. Floor Method : This method rounds DOWN number a to the nearest integer, and returns the result. 
Syntax

        math.floor(<value>)


04. Absolute value Method : This method returns the absolute value of a number.
Syntax

        math.fabs(<value>)

05. Power Method : This method returns the value of a numer raised to a base-number.
Syntax

        math.pow(base, exponent)

        where base is the value on which exponentiation is to be done.
        and exponent is the value which is to be raised on the base. 


06. Remainder Method : This method returns the closest value which can make numerator completely divisible by the denominator.
Syntax

        math.remainder(<numerator>, <denominator>)


07. Greatest Common Divisor : This method returns the gcd of two integers 
Syntax

        math.gcd(x, y)

        where x & y are the two numbers whose gcd needs to be find.

        also known as HCF


08. fmod() Method : It gives the remainder of x / y
Syntax

        math.fmod(x, y)


09. fsum() Method : It returns the sum of all elemnts in any iterable (tuples, arrays, lists, etc.)
Syntax

        math.fsum(<iterable>)

10. Product Method : It returns the product of all elements in any iterable.

        math.prod(<iterable>)


11. isclose() Method : This method checks if two number-values are close to each other or not.
Syntax

        math.isclose(x, y)


12. Degrees to Radians : This methof converts the angle-in-degrees to angle-in-radians.
Syntax

        math.degrees()


13. Radians to Degrees : This method converts the radian measure of an angle to its degree measure.
Syntax

        math.radians()


14. Factorial Method : This method returns the factorial value of a number.
Syntax

        math.factorial(<factorial>)


15. Permutation Method : This method returns the number of ways to choose 'k' items from 'n' items with order & without any repetition. Just like the formulae given in books.
Syntax

        math.perm(n, k)

        where n is total items to choose from
        and k is total items to choose

16. Combination Method : This method returns the number of ways of getting 'k' unordered outcomes from 'n' possibilities, without repetition. Just like books formula.
Syntax        

        math.comb(n, k)

        where n is total items to choose from
        and k is total items to choose