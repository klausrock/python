
""" 
                                                        Return
Function    Signature	                Accepts	        Type    Purpose
                                                        	
ascii()     ascii(obj)	                Varies	        str	    ASCII  only representation of an object, with non-ASCII characters escaped

bin()	    bin(number)	                number: int	    str	    Binary representation of an integer, with the prefix "0b"
hex()	    hex(number)	                number: int	    str	    Hexadecimal representation of an integer, with the prefix "0x"
oct()	    oct(number)	                number: int	    str	    Octal representation of an integer, with the prefix "0o"

bytes()	    bytes(iterable_of_ints)     Varies          bytes   Coerce (convert) the input to bytes, raw binary data
            bytes(s, enc[, errors])     
            bytes(bytes_or_buffer) 
            bytes([i])	                		

chr()	    chr(i)	                    i: int          str	    Convert an integer code point to a single Unicode character
            i>=0
            i<=1114111	

int()	    int([x])                    Varies	        int	    Coerce (convert) the input to int
            int(x, base=10)

ord()	    ord(c)	                    c: str
                                        len(c) == 1	    int	    Convert a single Unicode character to its integer code point
str()	    str(object='')
            str(b[, enc[, errors]])	    Varies	        str	    Coerce (convert) the input to str, text
"""

# From lib/python3.7/string.py

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

print(int('11'))
print(int('11', base=10))
print(int('11', base=2))
print(int('11', base=8))
print(int('11', base=16))

print('----------------------')

print(0b11)  # Binary literal
print(0o11)  # Octal literal
print(0x11)  # Hex literal

# Example ascii() - gives you an ASCII-only representation of an object, with non-ASCII characters escaped:

print("\nascii()\n")

print(ascii("abcdefg"))
print(ascii("jalepeño"))
print(ascii((1, 2, 3)))
print(ascii(0xc0ffee))  # Hex literal (int))

# Example bin() - gives you a binary representation of an integer, with the prefix "0b":

print("\nbin()\n")

print(bin(0))
print(bin(400))
print(bin(0xc0ffee))                        # Hex literal (int)
print([bin(i) for i in [1, 2, 4, 8, 16]])  # `int` + list comprehension

# Example bytes() coerces the input to bytes, representing raw binary data:

print("\nbytes()\n")

print(bytes((104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100)))    # Iterable of ints
print(bytes("real 🐍", "utf-8"))                                        # String + encoding
print(bytes(10))
print(bytes.fromhex('c0 ff ee'))
print(bytes.fromhex("72 65 61 6c 70 79 74 68 6f 6e"))

# Example chr() converts an integer code point to a single Unicode character:

print("\nchr()\n")

print(chr(97))
print(chr(7048))
print(chr(1114111))
print(chr(0x10FFFF))    # Hex literal (int)
print(chr(0b01100100))  # Binary literal (int)

# Example hex() gives the hexadecimal representation of an integer, with the prefix "0x":

print("\nhex()\n")

print(hex(100))
print([hex(i) for i in [1, 2, 4, 8, 16]])
print([hex(i) for i in range(16)])

# Example int() coerces the input to int, optionally interpreting the input in a given base:

print("\nint()\n")

print(int(11.0))
print(int('11'))
print(int('11', base=2))
print(int('11', base=8))
print(int('11', base=16))
print(int(0xc0ffee - 1.0))
print(int.from_bytes(b"\x0f", "little"))
print(int.from_bytes(b'\xc0\xff\xee', "big"))

# Example ord() function converts a single Unicode character to its integer code point:

print("\nord()\n")

print(ord("a"))
print(ord("ę"))
print(ord("ᮈ"))
print([ord(i) for i in "hello world"])

# Example str() coerces the input to str, representing text:

print("\nstr()\n")

print(str("str of string"))
print(str(5))
print(str([1, 2, 3, 4]))  # Like [1, 2, 3, 4].__str__(), but use str()
print(str(b"\xc2\xbc cup of flour", "utf-8"))
print(str(0xc0ffee))




