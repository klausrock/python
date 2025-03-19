"""
Function Annotations

def func(arg: arg_type, optarg: arg_type = default) -> return_type:
    ...

When running the code, you can also inspect the annotations. 
They are stored in a special .__annotations__ attribute on the function:    

Variable Annotations

variable: type = 3.142

Annotations of variables are stored in the module level __annotations__ dictionary:

"""

import math

def hello_name(name: str) -> str:
    return(f"Hello {name}")

def circumference(radius: float) -> float:
    return 2 * math.pi * radius

print(circumference.__annotations__)
print(circumference(1.23))

pi: float = 3.142
payload: []
name: str = "Klaus" 
print(__annotations__)
