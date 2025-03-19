""" 
Arithmetic Operators in Python

https://static.realpython.com/guides/python-operators.pdf
https://realpython.com/python-operators-expressions/

"""

42 == 42
print(42==42)

# Assignment Operator

number = 42
day = "Friday"
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
letters = ["a", "b", "c"]

""" 
Arithmetic Operators and Expressions
------------------------------------

Operator Type	Operation	    Sample      Result
                                Expression	

+	    Unary	Positive	    +a	        a without any transformation since this is simply a complement to negation
+	    Binary	Addition	    a + b	    The arithmetic sum of a and b
-	    Unary	Negation	    -a	        The value of a but with the opposite sign
-	    Binary	Subtraction	    a - b	    b subtracted from a
*	    Binary	Multiplication	a * b	    The product of a and b
/	    Binary	Division	    a / b	    The quotient of a divided by b, expressed as a float
%	    Binary	Modulo	        a % b	    The remainder of a divided by b
//	    Binary	Floor division  a // b	    The quotient of a divided by b, rounded to the next smallest whole number
**	    Binary	Exponentiation	a**b	    a raised to the power of b
"""

a = 5
b = 2

+a
# >>> 5

-b
# >>> -2

a + b
# >>> 7

a - b
# >>> 3

a * b
# >>> 10

a / b
# >>> 2.5

a % b
# >>> 1

a // b
# >>> 2

a**b
# >>> 25

""" 
Comparison Operators and Expressions
------------------------------------

Operator	Operation	    Sample      Result
                            Expression	

==	        Equal to	        a == b	• True if the value of a is equal to the value of b
                                        • False otherwise
!=	        Not equal to	    a != b	• True if a isn't equal to b
                                        • False otherwise
<	        Less than	        a < b	• True if a is less than b
                                        • False otherwise
<=	        Less than           a <= b	• True if a is less than or equal to b
            or equal to	                • False otherwise
>	        Greater than	    a > b	• True if a is greater than b
                                        • False otherwise
>=	Greater than or equal to	a >= b	• True if a is greater than or equal to b
                                        • False otherwise
"""

2 == "2"
# >>> False

"""
Comparison of Integer Values
----------------------------
"""

a = 10
b = 20

a == b
# >>> False

a != b
# >>> True

a < b
# >>> True

a <= b
# >>> True

a > b
# >>> False

a >= b
# >>> False

x = 30
y = 30

x == y
# >>> True

x != y
# >>> False

x < y
# >>> False

x <= y
# >>> True

x > y
# >>> False

x >= y
# >>> True

""" 
Comparison of Floating-Point Values
-----------------------------------
"""

x = 1.1 + 2.2

x == 3.3
# >>> False

1.1 + 2.2
# >>> 3.3000000000000003

""" 
The math module from the standard library provides a function conveniently called 

isclose() 

that will help you with float comparison. 
The function takes two numbers and tests them for approximate equality:

https://realpython.com/python-math-module/#find-the-closeness-of-numbers-with-python-isclose
"""

from math import isclose

x = 1.1 + 2.2

isclose(x, 3.3)
# >>> True

""" 
Comparison of Strings
---------------------
Python compares strings character by character using each character's 
Unicode code point. Unicode is Python's default character set.

You can use the built-in ord() function to learn the Unicode code point of any 
character in Python. Consider the following examples:

ord(c)
Given a string representing one Unicode character, return an integer representing 
the Unicode code point of that character. 

For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. 
This is the inverse of chr().
"""

ord("A")
# >>> 65

ord("a")
# >>> 97

"A" == "a"
# >>> False

"A" > "a"
# >>> False

"A" < "a"
# >>> True

"Hello" > "HellO"
# >>> True

ord("o")
# >>> 111
ord("O")
# >>> 79

"Hello" > "Hello, World!"
# >>> False

""" 
Comparison of Lists and Tuples
------------------------------

When comparing these data types, Python runs an item-by-item comparison.

It's important to note that you can actually compare lists to tuples using 
the == and != operators. 

However, you can't compare lists and tuples using the <, >, <=, and >= operators:
"""

[2, 3] == [2, 3]
# >>> True

(2, 3) == (2, 3)
# >>> True

[5, 6, 7] < [7, 5, 6]
# >>> True

(5, 6, 7) < (7, 5, 6)
# >>> True

[4, 3, 2] < [4, 3, 2]
# >>> False

(4, 3, 2) < (4, 3, 2)
# >>> False

[2, 3] == (2, 3)
# >>> False

[2, 3] != (2, 3)
# >>> True

# You can also compare lists and tuples of different lengths:

[5, 6, 7] < [8]
# >>> True

(5, 6, 7) < (8,)
# >>> True

[5, 6, 7] == [5]
# >>> False

(5, 6, 7) == (5,)
# >>> False

[5, 6, 7] > [5]
# >>> True

(5, 6, 7) > (5,)
# >>> True

""" 
Boolean Operators and Expressions in Python
-------------------------------------------

Python has three Boolean or logical operators: and, or, and not. 
They define a set of operations denoted by the generic operators AND, OR, and NOT. 
With these operators, you can create compound conditions.

https://realpython.com/python-return-statement/#returning-true-or-false

Operator	Sample Expression	Result
and	        x and y	            • True if both x and y are True
                                • False otherwise
or	        x or y	            • True if either x or y is True
                                • False otherwise
not	        not x	            • True if x is False
                                • False if x is True
"""

age = 20

is_adult = age > 18
is_adult
# >>> True

type(is_adult)
# >>> <class 'bool'>

# and Operator

5 < 7 and 3 == 3
# >>> True

5 < 7 and 3 != 3
# >>> False

5 > 7 and 3 == 3
# >>> False

5 > 7 and 3 != 3
# >>> False

# or Operator

5 < 7 or 3 == 3
# >>> True

5 < 7 or 3 != 3
# >>> True

5 > 7 or 3 == 3
# >>> True

5 > 7 or 3 != 3
# >>> False

# not operator

5 < 7
# >>> True

not 5 < 7
# >>> False

""" 
Evaluation of Regular Objects in a Boolean Context
--------------------------------------------------

In practice, most Python objects and expressions aren't Boolean. 
In other words, most objects and expressions don't have a True or False value 
but a different type of value. 

However, you can use any Python object in a Boolean context, such as a conditional 
statement or a while loop.

In Python, all objects have a specific truth value. 
So, you can use the logical operators with all types of operands.

By default, an object is considered true unless its class defines either 
a __bool__() method that returns False or a __len__() method that returns zero, 
when called with the object. 

Here are most of the built-in objects considered false:

    constants defined to be false: None and False.
    zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
    empty sequences and collections: '', (), [], {}, set(), range(0)

You can determine the truth value of an object by calling the 
built-in bool() function with that object as an argument. 
If bool() returns True, then the object is truthy. 
If bool() returns False, then it's falsy.
"""

bool(0), bool(0.0), bool(0.0+0j)
# >>> (False, False, False)

bool(-3), bool(3.14159), bool(1.0+1j)
# >>> (True, True, True)

bool("")
# >>> False

bool(" ")
# >>> True

bool("Hello")
# >>> True

bool([])
# >>> False

bool([1, 2, 3])
# >>> True

bool(())
# >>> False

bool(("John", 25, "Python Dev"))
# >>> True

bool(set())
# >>> False

bool({"square", "circle", "triangle"})
# >>> True

bool({})
# >>> False

bool({"name": "John", "age": 25, "job": "Python Dev"})
# >>> True

""" 
Boolean Expressions Involving Other Types of Operands
-----------------------------------------------------

To start off, below is a table that summarizes what you get when you use two objects,
x and y, in an and expression:

If x is	    x and y returns

Truthy	    y
Falsy	    x
"""

3 and 4
# >>> 4

0 and 4
# >>> 0

3 and 0
# >>> 0

