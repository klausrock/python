"""
#
# Global Variables in Your Python Functions
# https://realpython.com/python-use-global-variable-in-function/
#
# Python  looks for variables in four different scopes:
#
# - The local, or function-level, scope, which exists inside functions
# - The enclosing, or non-local, scope, which appears in nested functions
# - The global scope, which exists at the module level
# - The built-in scope, which is a special scope for Python’s built-in names
#
"""

number = 42

def access_number():
    return number

print(access_number())
# >>>42

def modify_number():
    number = 7

print(modify_number())
print(number)
# >>> 42

a = 10
b = 20
c = 30

def print_globals():
    print(a, b, c)
    # c = 100 !!!
    print(c)

print(print_globals())
# >>>10 20 30
# >>>100

""" 
#
# If you want to modify a global variable inside a function, 
# then you need to explicitly tell Python to use the 
# global variable rather than creating a new local one. 
# To do this, you can use one of the following:
#
# 1. The global keyword
# 2. The built-in globals() function
#
# global variable_0, variable_1, ..., variable_n
#
"""

counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)
# >>>1

increment()
print(counter)
# >>>2

""" 
#
# The globals() Function
#
# The built-in globals() function allows you to access the 
# global scope’s name table, which is a writable dictionary 
# containing your current global names and their corresponding values. 
# You can use this function to either access or modify the value of a 
# global variable from within your functions.
#
"""

a = 10
b = 20
c = 30

def print_globals():
    print(a, b, globals()["c"])
    c = 100
    print(c)

print_globals()
# >>>10 20 30
# >>>100

print(c)
# >>>30

counter = 0

def increment():
    globals()["counter"] += 1

increment()
print(counter)
# >>>1

increment()
print(counter)
# >>>2




