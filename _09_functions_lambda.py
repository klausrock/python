""" 
Anonymous (lambda) Functions
https://realpython.com/python-lambda/

lambda arguments : expression

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, 
but can only have one expression.

"""

def identity(x):
    return x
# =

#
lambda x: x
lambda x: x + 1

# In the current example, it consists of replacing the bound variable 
# x with the argument 2:

(lambda x: x + 1)(2)

# (lambda x: x + 1)(2) = lambda 2: 2 + 1
#                      = 2 + 1
#                      = 3

add_one = lambda x: x + 1
print(add_one(2))

# =

def add_one(x):
    return x + 1

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))
# >>> Full name: Guido Van Rossum'

# You can invoke the function in the Python interpreter:

# lambda x, y: x + y
# _(1, 2)
# >>> 3

print((lambda x, y: x + y)(2, 3))
# >>> 5

# Higher-order function by taking a function

high_ord_func = lambda x, func: x + func(x)

print(high_ord_func(2, lambda x: x * x))
# >>> 6

print(high_ord_func(2, lambda x: x + 3))
# >>> 7

""" 
The following examples illustrate options open to you in order to pass 
arguments to lambda expressions:
"""

print((lambda x, y, z: x + y + z)(1, 2, 3))
# >>> 6

print((lambda x, y, z=3: x + y + z)(1, 2))
# >>> 6

print((lambda x, y, z=3: x + y + z)(1, y=2))
# >>> 6

print((lambda *args: sum(args))(1,2,3))
# >>> 6

print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
# >>> 6

print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
# >>> 6

""" 
So why would you ever want to use such a thing? Primarily, 
it comes down to the fact that everything is an object in Python, 
even functions themselves! 

That means that functions can be passed as arguments to functions.
"""

data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},  
{'first':'Grace', 'last':'Hopper',  'YOB':1906},
{'first':'Alan',  'last':'Turing',  'YOB':1912}]

# dictionaries are not orderable: 
# we need a way to tell the function how to sort our data. 
# We can do this by specifying the key function, a function which 
# given an item returns the sorting key for that item:


# sort alphabetically by first name
sorted(data, key=lambda item: item['first'])

# >>> [{'YOB': 1912, 'first': 'Alan', 'last': 'Turing'},
# >>>  {'YOB': 1906, 'first': 'Grace', 'last': 'Hopper'},
# >>>  {'YOB': 1956, 'first': 'Guido', 'last': 'Van Rossum'}]

# # sort by year of birth
sorted(data, key=lambda item: item['YOB'])

# >>> [{'YOB': 1906, 'first': 'Grace', 'last': 'Hopper'},
# >>>  {'YOB': 1912, 'first': 'Alan', 'last': 'Turing'},
# >>>  {'YOB': 1956, 'first': 'Guido', 'last': 'Van Rossum'}]



