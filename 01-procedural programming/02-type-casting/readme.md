# Type Casting In Python

* Type casting in python is a method of converting values of one data-type to another data type, if possible.

* Type Casting can be classified into two types ~

Implicit Typecasting || Explicit Typecasting

01. **_Implicit Typecasting_** : Implicit Typecasting is the type-casting done automatically by the python interpreter.

02. **_Explicit Typecasting_** : Explicit Typecasting is the manual process of converting value of one data-type into other, if possible.

_Note_ - There is a function called **_type()_** function in python, that can tell us the data-type of any value.

**_Syntax Of Usage -_**
```python
a = 5
printf( type(a) )
```
```powershell
<class 'int'>
```

```python
b = 6.3
printf( type(b) )
```
```powershell
<class 'float'>
```

```python
c = 'Hello'
printf( type(c) )
```
```powershell
<class 'string'>
```
-------------------------------------------------

There are a bunch of things that are needed to be kept in mind while performing explicit typecasting.

01. It is not mandatory that whatever type-casting you are trying to do will surely happen! So make sure what you are type-casting into.

02. There are bunch of things that are convertible. They are ~

    ***a) integer value to a floating-point value.***
    ```python
    a = 5
    print(a, " || ", type(a))
    ```
    ```powershell
    5 || <class 'int'>
    ```

    ```python
    b = float(a)
    print(b, " || ", type(b))
    ```
    ```powershell
    5.0 || <class 'float'>
    ``` 


    ***b) integer value to a string value.***
    ```python
    a = 5
    print(a, " || ", type(a))
    ```
    ```powershell
    5 || <class 'int'>
    ``` 

    ```python
    b = float(a)
    print(b, " || ", type(b))
    ```
    ```powershell
    "5" || <class 'string'>
    ```

    ***c) floating-point value to a integer value.***
    ```python
    a = 5.6
    print(a, " || ", type(a))
    ```
    ```powershell 
    5.6 || <class 'float'>
    ```

    ```python
    b = int(a)
    print(b, " || ", type(b))
    ```
    ```powershell
    "5" || <class 'int'>
    ```
    Notice how it removes the decimal part of the original value.

    ***d) floating-point value to a string value.***
    ```python
    a = 5.36
    print(a, " || ", type(a))
    ```
    ```powershell
    5.36 || <class 'float'>
    ```

    ```python
    b = float(a)
    print(b, " || ", type(b))
    ```
    ```powershell
    "5.36" || <class 'string'>
    ```

    ***e) string values to integer and floating-point values.***

    *// string to integer //*
    ```python
    a = "5"
    print(a, " || ", type(a))
    ```
    ```powershell
    "5" || <class 'string'>
    ```

    ```python
    b = int(a)
    print(b, " || ", type(b))
    ```

    ```powershell
    5 || <class 'int'>
    ```

    *// string to floating-point //*
    ```python
    a = "5"
    print(a, " || ", type(a))
    ```
    ```powershell
    "5" || <class 'string'>
    ```

    ```python
    b = float(a)
    print(b, " || ", type(b))
    ```
    ```powershell
    5.0 || <class 'float'>
    ```

    ```python
    #                       important ones
    ```

    ```python
    name = 'ankur'
    printf(name, " || ", type(name))
    ```
    ```powershell
    'ankur' || <class 'string'>
    ```

    ```python
    name = int(name) or float(name)
    printf(name, " || ", type(name))
    ```
    ```powershell
    ValueError: invalid literal for int() or float()
    ```