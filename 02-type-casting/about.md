                                    Type Casting In Python

* Type casting in python is a method of converting values of one data-type to another data type, if possible.

* Type Casting can be classified into two types ~

Implicit Typecasting || Explicit Typecasting

* Implicit Typecasting

    Implicit Typecasting is the type-casting done automatically by the python interpreter.

* Explicit Typecasting

    Explicit Typecasting is the manual process of converting value of one data-type into other, if possible.

Note - There is a function called type() function in python, that can tell us the data-type of any value.

Syntax Of Usage -

    a = 5
    printf( type(a) )

    >>> <class 'int'>


    b = 6.3
    printf( type(b) )

    >>> <class 'float'>


    c = 'Hello'
    printf( type(c) )

    >>> <class 'string'>

There are a bunch of things that are needed to be kept in mind while performing explicit types-casting.

01. It is not mandatory that whatever type-casting you are trying to do will surely happen! So make sure what you are type-casting into.

02. There are bunch of things that are convertible. They are ~

    a) integer value to a floating-point value.

        a = 5
        print(a, " || ", type(a))

        >>> 5 || <class 'int'>

        b = float(a)
        print(b, " || ", type(b))

        >>> 5.0 || <class 'float'>

    b) integer value to a string value.

        a = 5
        print(a, " || ", type(a))

        >>> 5 || <class 'int'>

        b = float(a)
        print(b, " || ", type(b))

        >>> "5" || <class 'string'>

    c) floating-point value to a integer value.

        a = 5.6
        print(a, " || ", type(a))

        >>> 5.6 || <class 'float'>
    
        b = int(a)
        print(b, " || ", type(b))

        >>> "5" || <class 'int'>
        <!-- Noticw how it removes the decimal part of the original value. -->
        
    d) floating-point value to a string value.
    
        a = 5.36
        print(a, " || ", type(a))

        >>> 5.36 || <class 'float'>

        b = float(a)
        print(b, " || ", type(b))

        >>> "5.36" || <class 'string'>


    e) string values to integer and floating-point values.

        // string to integer

        a = "5"
        print(a, " || ", type(a))

        >>> "5" || <class 'string'>

        b = int(a)
        print(b, " || ", type(b))

        >>> 5 || <class 'int'>

        // string to floating-point

        a = "5"
        print(a, " || ", type(a))

        >>> "5" || <class 'string'>

        b = float(a)
        print(b, " || ", type(b))

        >>> 5.0 || <class 'float'>

        name = 'ankur'
        printf(name, " || ", type(name))

        >>> 'ankur' || <class 'string'>

        name = int(name) or float(name)
        printf(name, " || ", type(name))

        >>> ValueError: invalid literal for int() or float()