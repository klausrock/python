# https://realpython.com/defining-your-own-python-function/

""" 
Defining

def <function_name>([<parameters>]):
    <statement(s)>

Calling

<function_name>([<arguments>])

"""

from matplotlib.widgets import EllipseSelector


s = 'foobar'
print(id(s))

a = ['foo', 'bar', 'baz', 'qux']
print(a,len(a))

# https://realpython.com/any-python/

any([False, False, False])
any([False, True, False])
any(['bar' == 'baz', len('foo') == 4, 'qux' in {'foo', 'bar', 'baz'}])
any(['bar' == 'baz', len('foo') == 3, 'qux' in {'foo', 'bar', 'baz'}])

"""
def read_file():
    # Code to read file in
    <statement>
    <statement>
    <statement>
    <statement>

def process_file():
    # Code to process file
    <statement>
    <statement>
    <statement>
    <statement>

def write_file():
    # Code to write file out
    <statement>
    <statement>
    <statement>
    <statement>

# Main program
read_file()
process_file()
write_file()
"""

# Argument Passing
# https://fstring.help/cheat/

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

# Positional Arguments

print(f(6, 'bananas', 1.74))

""" 
Using keyword arguments lifts the restriction on argument order. 
Each keyword argument explicitly designates a specific parameter by name,
so you can specify them in any order and Python will still know which 
argument goes with which parameter:
"""

# Keyword Arguments

print(f(item='bananas', price=1.74, qty=6))

# Default Parameters

def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')

print(f(4, 'apples', 2.24))
# >>> 4 apples cost $2.24

print(f(4, 'apples'))
# >>> 4 apples cost $1.74

print(f(4))
# >>> bananas cost $1.74

print(f())
# >>> 6 bananas cost $1.74

print(f(item='kumquats', qty=9))
# >>> 9 kumquats cost $1.74

print(f(price=2.29))
# >>> 6 bananas cost $2.29

# Mutable Default Parameter Values

def f(my_list=[]):
    print(id(my_list))
    my_list.append('###')
    return my_list

print(f())
# 140095566958408
# ['###'] 
       
print(f())
# 140095566958408
# ['###', '###']

print(f())
140095566958408
# ['###', '###', '###']

# Work around

def f(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append('###')
    return my_list

# The return Statement

""" 
def f():
    if error_cond1:
        return
    if error_cond2:
        return
    if error_cond3:
        return

    <normal processing>
"""

def f():
    return dict(foo=1, bar=2, baz=3)

print(f())
# >>> {'foo': 1, 'bar': 2, 'baz': 3}

print(f()['baz'])

def f():
    return 'foobar'

print(f()[2:4])
# >>> 'ob'

def f():
    return ['foo', 'bar', 'baz', 'qux']

print(f())
# >>> ['foo', 'bar', 'baz', 'qux']

print(f()[2])
# >>> 'baz'

print(f()[::-1])
# >>> ['qux', 'baz', 'bar', 'foo']

def f():
    return 'foo', 'bar', 'baz', 'qux'

print(type(f()))
# >>> <class 'tuple'>

t = f()
print(t)
# >>> ('foo', 'bar', 'baz', 'qux')

a, b, c, d = f()
print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# >>> a = foo, b = bar, c = baz, d = qux

# When no return value is given, a Python function returns the 
# special Python value None:

def f():
    return

print(f())
# >>> None

# Variable-Length Argument Lists

def avg(a, b, c):
    return (a + b + c) / 3

avg(1, 2, 3)
# >>> 2.0

def avg(a):
    total = 0
    for v in a:
        total += v
    return total / len(a)

avg([1, 2, 3])
# >>> 2.0  

avg([1, 2, 3, 4, 5])
# >>> 3.0  

t = (1, 2, 3, 4, 5)
print(avg(t))
# >>> 3.0

# Argument Tuple Packing
""" 
When a parameter name in a Python function definition is preceded by 
an asterisk (*), it indicates argument tuple packing. 
Any corresponding arguments in the function call are packed into a 
tuple that the function can refer to by the given parameter name. 

Here is an example:
"""

def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)

f(1, 2, 3)
# >>> (1, 2, 3)        
# >>> <class 'tuple'> 3
# >>> 1
# >>> 2
# >>> 3

f('foo', 'bar', 'baz', 'qux', 'quux')
# >>> ('foo', 'bar', 'baz', 'qux', 'quux')
# >>> <class 'tuple'> 5
# >>> foo
# >>> bar
# >>> baz
# >>> qux
# >>> quux

# Using tuple packing, you can clean up avg() like this:

def avg(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

print(avg(1, 2, 3))
# >>> 2.0

print(avg(1, 2, 3, 4, 5))
# >>> 3.0

def avg(*args):
    return sum(args) / len(args)

print(avg(1, 2, 3))
# >>> 2.0

print(avg(1, 2, 3, 4, 5))
# >>> 3.0

# Argument Tuple Unpacking

def f(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')

f(1, 2, 3)

# >>> x = 1
# >>> y = 2
# >>> z = 3

t = ('foo', 'bar', 'baz')
f(*t)
# >>> x = foo
# >>> y = bar
# >>> z = baz

a = ['foo', 'bar', 'baz']
print(type(a))
# >>> <class 'list'>

f(*a)
# >>> x = foo
# >>> y = bar
# >>> z = baz

s = {1, 2, 3}
print(type(s))
# >>> <class 'set'>

f(*s)
# >>> x = 1
# >>> y = 2
# >>> z = 3

def f(*args):
    print(type(args), args)

a = ['foo', 'bar', 'baz', 'qux']
f(*a)
# >>> <class 'tuple'> ('foo', 'bar', 'baz', 'qux')

# Argument Dictionary Packing

def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
        print(key, '->', val)

f(foo=1, bar=2, baz=3)
# >>> {'foo': 1, 'bar': 2, 'baz': 3}
# >>> <class 'dict'>
# >>> foo -> 1
# >>> bar -> 2
# >>> baz -> 3

# Argument Dictionary Unpacking

def f(a, b, c):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'c = {c}')

d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)
# >>> a = foo
# >>> b = 25
# >>> c = qux

f(a='foo', b=25, c='qux')
# >>> a = foo
# >>> b = 25
# >>> c = qux

f(**dict(a='foo', b=25, c='qux'))
# >>> a = foo
# >>> b = 25
# >>> c = qux

# Putting It All Together

def f(a, b, *args, **kwargs):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'args = {args}')
    print(F'kwargs = {kwargs}')

f(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)
# >>> a = 1
# >>> b = 2
# >>> args = ('foo', 'bar', 'baz', 'qux')
# >>> kwargs = {'x': 100, 'y': 200, 'z': 300}

# Multiple Unpackings in a Python Function Call

def f(*args):
    for i in args:
        print(i)

a = [1, 2, 3]
t = (4, 5, 6)
s = {7, 8, 9}

f(*a, *t, *s)
# >>> 1
# >>> 2
# >>> 3
# >>> 4
# >>> 5
# >>> 6
# >>> 8
# >>> 9
# >>> 7

def f(**kwargs):
    for k, v in kwargs.items():
        print(k, '->', v)

d1 = {'a': 1, 'b': 2}
d2 = {'x': 3, 'y': 4}

f(**d1, **d2)
# >>> a -> 1
# >>> b -> 2
# >>> x -> 3
# >>> y -> 4

def f(*args):
    for i in args:
        print(i)

f(*[1, 2, 3], *[4, 5, 6])
# >>> 1
# >>> 2
# >>> 3
# >>> 4
# >>> 5
# >>> 6

def f(**kwargs):
    for k, v in kwargs.items():
        print(k, '->', v)

f(**{'a': 1, 'b': 2}, **{'x': 3, 'y': 4})
# >>> a -> 1
# >>> b -> 2
# >>> x -> 3
# >>> y -> 4

# Keyword-Only Arguments
# https://www.youtube.com/watch?v=R8-oAqCgHag

def concat(*args):
    print(f'-> {".".join(args)}')

concat('a', 'b', 'c')
# >>> a.b.c

concat('foo', 'bar', 'baz', 'qux')
# >>> foo.bar.baz.qux

def concat(prefix, *args):
    print(f'{prefix}{".".join(args)}')

concat('//', 'a', 'b', 'c')
# >>> //a.b.c

concat('... ', 'foo', 'bar', 'baz', 'qux')
# >>> ... foo.bar.baz.qux

def concat(*args, prefix='-> '):
    print(f'{prefix}{".".join(args)}')

concat('a', 'b', 'c', prefix='... ')
# >>> ... a.b.c

def concat(*args, prefix='-> ', sep='.'):
    print(f'{prefix}{sep.join(args)}')

concat('a', 'b', 'c')
# >>> -> a.b.c

concat('a', 'b', 'c', prefix='//')

# >>> //a.b.c

concat('a', 'b', 'c', prefix='//', sep='-')

# >>> //a-b-c

"""
The bare variable argument parameter * indicates that there aren't 
any more positional parameters. This behavior generates appropriate 
error messages if extra ones are specified. 
It allows keyword-only parameters to follow.
"""

def oper(x, y, *, op='+'):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y
    else:
        return None

oper(3, 4, op='+')
# >>> 7

oper(3, 4, op='/')
# >>> 0.75

# Positional-Only Arguments

""" 
To designate some parameters as positional-only, you specify a bare slash
(/) in the parameter list of a function definition. Any parameters to the
left of the slash (/) must be specified positionally. 
For example, in the following function definition, x and y are positional
-only parameters, but z may be specified by keyword:
"""

# This is Python 3.8
# def f(x, y, /, z):
#     print(f'x: {x}')
#     print(f'y: {y}')
#     print(f'z: {z}')

# This is Python 3.8
# def f(x, y, /, z, w, *, a, b):
#     print(x, y, z, w, a, b)

f(1, 2, z=3, w=4, a=5, b=6)
# >>> 1 2 3 4 5 6

f(1, 2, 3, w=4, a=5, b=6)
# >>> 1 2 3 4 5 6

# Docstrings

""" 
When the first statement in the body of a Python function is a string 
literal, it’s known as the function’s docstring. A docstring is used to 
supply documentation for a function. It can contain the function's 
purpose, what arguments it takes, information about return values, 
or any other information you think would be useful.
"""

def foo(bar=0, baz=1):
    """
    Perform a foo transformation.
    Keyword arguments:
    bar -- magnitude along the bar axis (default=0)
    baz -- magnitude along the baz axis (default=1)
    """
#<function_body>

print(foo.__doc__)

# >>> Perform a foo transformation.
# >>> 
# >>>     Keyword arguments:
# >>>     bar -- magnitude along the bar axis (default=0)
# >>>     baz -- magnitude along the baz axis (default=1)

# In the interactive Python interpreter, you can type 
# help(<function_name>) 
# to display the docstring for <function_name>:

help(foo)

# >>> Help on function foo in module __main__:
# >>> 
# >>> foo(bar=0, baz=1)
# >>>     Perform a foo transformation.
# >>> 
# >>>    Keyword arguments:
# >>>    bar -- magnitude along the bar axis (default=0)
# >>>    baz -- magnitude along the baz axis (default=1)

# Annotations - New in Python 3.0

def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        b, a = a + b, b
    return a

print("\n",fib(10))

# def f(a: '<a>', b: '<b>') -> '<ret_value>':
#     pass

f.__annotations__
# >>> {'a': '<a>', 'b': '<b>', 'return': '<ret_value>'}

f.__annotations__['a']
# >>> '<a>'
f.__annotations__['b']
# >>> '<b>'
f.__annotations__['return']
# >>> '<ret_value>

# Note that annotations aren’t restricted to string values. 
# They can be any expression or object. For example, 
# you might annotate with type objects:

def f(a: int, b: str) -> float:
    print(a, b)
    return(3.5)

f(1, 'foo')
# >>> 1 foo
# >>> 3.5

f.__annotations__
# >>> {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}

# Default Values

def f(a: int = 12, b: str = 'baz') -> float:
    print(a, b)
    return(3.5)

f.__annotations__
# >>> {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}

f()
# >>> 12 baz
# >>> 3.5

#