"""
Built-In Data Structures
We have seen Python's simple types: int, float, complex, bool, str, ...
Python also has several built-in compound types, which act as containers 
for other types. 

These compound types are:

Type Name	Example	                Description
-------------------------------------------------------------------------

list	    [1, 2, 3]	            Ordered collection
tuple	    (1, 2, 3)	            Immutable ordered collection
dict	    {'a':1, 'b':2, 'c':3}	Unordered (key,value) mapping
set	        {1, 2, 3}	            Unordered collection of unique values

https://realpython.com/python-lists-tuples/
https://nbviewer.org/github/jakevdp/WhirlwindTourOfPython/blob/master/06-Built-in-Data-Structures.ipynb
"""

"""
Lists
-----

Lists are the basic ordered and mutable data collection type in Python.
They can be defined with comma-separated values between square brackets;
for example, here is a list of the first several prime numbers:
"""

L = [2, 3, 5, 7]

# Length of a list
len(L)

# Append a value to the end
L.append(11)
L

# Addition concatenates lists
L + [13, 17, 19]

# sort() method sorts in-place
L = [2, 5, 1, 6, 3, 4]
L.sort()
L

# Can contain any Object
L = [1, 'two', 3.14, [0, 3, 5]]

""" 
List indexing and slicing
-------------------------
"""

L = [2, 3, 5, 7, 11]
L[0]
# >>> 2

L[1]
# >>> 3

# Elements at the end of the list can be accessed with negative numbers, 
# starting from -1:

L[-1]
# >>> 11

L[-2]
# >>> 7

""" 
Slicing is a means of accessing multiple values in sub-lists
"""

L[0:3]
[2, 3, 5]

# Notice where 0 and 3 lie in the preceding diagram, and how the slice 
# takes just the values between the indices. If we leave out the first 
# index, 0 is assumed, so we can equivalently write:

L[:3]
# >>> [2, 3, 5]

# Similarly, if we leave out the last index, it defaults to the length 
## of the list. Thus, the last three elements can be accessed as follows:

L[-3:]
# >>> [5, 7, 11]

# Finally, it is possible to specify a third integer that represents 
# the step size; for example, to select every second element of the list,
# we can write:

L[::2]  # equivalent to L[0:len(L):2]
# >>> [2, 5, 11]

# A particularly useful version of this is to specify a negative step, 
# which will reverse the array:

L[::-1]
# >>> [11, 7, 5, 3, 2]

# Both indexing and slicing can be used to set elements as well as access
# them. The syntax is as you would expect:

L[0] = 100
print(L)
# >>> [100, 3, 5, 7, 11]

L[1:3] = [55, 56]
print(L)
# >>> [100, 55, 56, 7, 11]

"""
Tuples
------
Tuples are in many ways similar to lists, but they are defined with 
parentheses rather than square brackets.

The main distinguishing feature of tuples is that they are immutable: 
this means that once they are created, their size and contents cannot 
be changed:
"""

t = (1, 2, 3)

# They can also be defined without any brackets at all:

t = 1, 2, 3
print(t)
# >>> (1, 2, 3)

# Like the lists discussed before, tuples have a length, and individual 
# elements can be extracted using square-bracket indexing:

len(t)
# >>> 3

t[0]
# >>> 1

# Tuples are often used in a Python program; a particularly common case 
# is in functions that have multiple return values

x = 0.125
x.as_integer_ratio()
# >>> (1, 8)

# These multiple return values can be individually assigned as follows:

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)
# >>> 0.125

# The indexing and slicing logic covered earlier for lists works for 
# tuples as well, along with a host of other methods. 
# Refer to the online Python documentation for a more complete list of 
# these.

"""
Dictionaries
------------

Dictionaries are extremely flexible mappings of keys to values, 
and form the basis of much of Python's internal implementation. 
They can be created via a comma-separated list of key:value pairs 
within curly braces:

"""

numbers = {'one':1, 'two':2, 'three':3}

# Items are accessed and set via the indexing syntax used for lists and 
# tuples, except here the index is not a zero-based order but 
# valid key in the dictionary:

# Access a value via the key

numbers['two']
2

# New items can be added to the dictionary using indexing as well:

# Set a new key:value pair

numbers['ninety'] = 90
print(numbers)

# >>> {'three': 3, 'ninety': 90, 'two': 2, 'one': 1}

# Keep in mind that dictionaries do not maintain any sense of order for 
# the input parameters; this is by design. 
# This lack of ordering allows dictionaries to be implemented 
# very efficiently, so that random element access is very fast, 
# regardless of the size of the dictionary 
# (if you're curious how this works, read about the concept of a 
# hash table). The python documentation has a complete list of the 
# methods available for dictionaries.

# Init
glossary = {"BDFL": "Benevolent Dictator For Life"}

# Add
glossary["GIL"] = "Global Interpreter Lock"  

# Update
glossary["BDFL"] = "Guido van Rossum"  

# Delete
del glossary["GIL"]

# Search
glossary["BDFL"]  
'Guido van Rossum'

glossary
{'BDFL': 'Guido van Rossum'}

""" 
Sets
----

The fourth basic collection is the set, which contains unordered 
collections of unique items. They are defined much like lists and tuples, 
except they use the curly brackets of dictionaries:

If you're familiar with the mathematics of sets, you'll be familiar 
with operations like the union, intersection, difference, 
symmetric difference, and others. 

Python's sets have all of these operations built-in, via methods or 
operators. 

For each, we'll show the two equivalent methods:
"""

primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}

# union: items appearing in either

primes | odds      # with an operator
primes.union(odds) # equivalently with a method
# >>> {1, 2, 3, 5, 7, 9}

# intersection: items appearing in both

primes & odds             # with an operator
primes.intersection(odds) # equivalently with a method
# >>> {3, 5, 7}

# difference: items in primes but not in odds

primes - odds           # with an operator
primes.difference(odds) # equivalently with a method
# >>> {2}

# symmetric difference: items appearing in only one set

primes ^ odds                     # with an operator
primes.symmetric_difference(odds) # equivalently with a method
# >>> {1, 2, 9}

# Many more set methods and operations are available. 
# You've probably already guessed what I'll say next: 
# refer to Python's online documentation for a complete reference.

