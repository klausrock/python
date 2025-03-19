""" 
In this tutorial, you'll explore regular expressions, 
also known as regexes, in Python. 

A regex is a special sequence of characters that defines 
a pattern for complex string-matching functionality.
https://realpython.com/regex-python/
"""

# There are at least a couple ways to do this. 
# You could use the in operator:

s = 'foo123bar'
'123' in s
# >>> True

# Each of these returns the character position within s 
# where the substring resides:

s = 'foo123bar'
s.find('123')
# >>> 3

s.index('123')
# >>> 3

""" 
The re Module
re.search(<regex>, <string>) | Scans a string for a regex match.
scans <string> looking for the first location where the pattern 
<regex> matches. 

If a match is found, then re.search() returns a match object. 
Otherwise, it returns None.
"""

import re
re.search(...)

from re import search
search(...)

# First Pattern-Matching Example

s = 'foo123bar'

# One last reminder to import!
import re

re.search('123', s)
# >>> <_sre.SRE_Match object; span=(3, 6), match='123'>

if re.search('123', s):
    print('Found a match.')
else:
    print('No match.')

# >>> Found a match.

s[3:6]
# >>> '123'

# The full expression [0-9][0-9][0-9] matches any sequence of 
# three decimal digit characters. 

re.search('[0-9][0-9][0-9]', 'foo456bar')
# >>> <_sre.SRE_Match object; span=(3, 6), match='456'>

re.search('[0-9][0-9][0-9]', '234baz')
# >>> <_sre.SRE_Match object; span=(0, 3), match='234'>

re.search('[0-9][0-9][0-9]', 'qux678')
# >>> <_sre.SRE_Match object; span=(3, 6), match='678'>

print(re.search('[0-9][0-9][0-9]', '12foo34'))
# >>> None

s = 'foo123bar'
re.search('1.3', s)
# >>> <_sre.SRE_Match object; span=(3, 6), match='123'>

s = 'foo13bar'
print(re.search('1.3', s))
# >>> None

# Metacharacters Supported by the re Module
# https://realpython.com/regex-python/#metacharacters-supported-by-the-re-module

# [] | Specifies a specific set of characters to match.

re.search('ba[artz]', 'foobarqux')
# >>> <_sre.SRE_Match object; span=(3, 6), match='bar'>

re.search('ba[artz]', 'foobazqux')
# >>> <_sre.SRE_Match object; span=(3, 6), match='baz'>
