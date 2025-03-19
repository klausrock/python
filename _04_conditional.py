# https://realpython.com/python-conditional-statements/

"""
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>
"""

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

"""
if <expr>:
    <statement(s)>
else:
    <statement(s)>

"""

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

"""
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
"""

name = 'Joe'

if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# Here’s one possible alternative

names = {
'Fred': 'Hello Fred',
'Xander': 'Hello Xander',
'Joe': 'Hello Joe',
'Arnold': 'Hello Arnold'
}

# https://realpython.com/python-dicts/#dgetkey-default
#
# dictionary.get(keyname, value)
#
# keyname Required. The keyname of the item you want to return the 
#                   value from
# value	Optional.   A value to return if the specified key does not exist.
#                   Default value None

print(names.get('Joe', "I don't know who you are!"))
# >>> Hello Joe

print(names.get('Rick', "I don't know who you are!"))
# >>>I don't know who you are!

"""
if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
"""

if 'f' in 'foo': print('1'); print('2'); print('3')
if 'z' in 'foo': print('1'); print('2'); print('3')

x = 2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

"""
Conditional Operator or Ternary Operator

<expr1> if <conditional_expr> else <expr2>

This is different from the if statement forms listed above because 
it is not a control structure that directs the flow of program execution.
 It acts more like an operator that defines an expression. 
 In the above example, <conditional_expr> is evaluated first.

 If it is true, the expression evaluates to <expr1>. 
 If it is false, the expression evaluates to <expr2>.

"""

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'minor' if age < 21 else 'adult'
print(s)

print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')

a=10;b=20
m = a if a > b else b
print(m)

x = y = 40

z = 1 + x if x > y else y + 2
print(z)

z = (1 + x) if x > y else (y + 2)
print(z)

x = y = 40
z = 1 + (x if x > y else y) + 2
print(z)

