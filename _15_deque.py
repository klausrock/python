
""" 
Building Efficient Queues and Stacks: deque
https://realpython.com/python-collections-module/#building-efficient-queues-and-stacks-deque
https://realpython.com/python-deque/

Note: 
The word deque is pronounced “deck” and stands for double-ended queue.

Python's collections module provides a class called deque that's specially
designed to provide fast and memory-efficient ways to append and pop 
item from both ends of the underlying data structure.
"""

from collections import deque

# Create an empty deque
deque()
# >>> deque([])

# Use different iterables to create deques
deque((1, 2, 3, 4))
# >>> deque([1, 2, 3, 4])

deque([1, 2, 3, 4])
# >>> deque([1, 2, 3, 4])

deque(range(1, 5))
# >>> deque([1, 2, 3, 4])

deque("abcd")
# >>> deque(['a', 'b', 'c', 'd'])

numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
deque(numbers.keys())
# >>> deque(['one', 'two', 'three', 'four'])

deque(numbers.values())
# >>> deque([1, 2, 3, 4])

deque(numbers.items())
# >>> deque([('one', 1), ('two', 2), ('three', 3), ('four', 4)]) 

""" 
Popping and Appending Items Efficiently

The most important difference between deque and list is that the former 
allows you to perform efficient append and pop operations on both ends 
of the sequence. 

The deque class implements dedicated .popleft() and .appendleft() methods
that operate on the left end of the sequence directly:
"""

from collections import deque
from time import perf_counter

numbers = deque([1, 2, 3, 4])
print(numbers.popleft())
# >>> 1

print(numbers.popleft())
# >>> 2

print(numbers)
# >>> deque([3, 4])

numbers.appendleft(2)
numbers.appendleft(1)
print(numbers)
# >>> deque([1, 2, 3, 4])

""" 
In this script, average_time() computes the average time that executing 
a function (func) a given number of times takes. 
"""

print('\nPerformace Test')
print('===============\n')

TIMES = 10_000
a_list = []
a_deque = deque()

def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        total += (perf_counter() - start) * 1e9
    return total / times

list_time = average_time(lambda i: a_list.insert(0, i), TIMES)
deque_time = average_time(lambda i: a_deque.appendleft(i), TIMES)
gain = list_time / deque_time

print(f"list.insert()      {TIMES} TIMES {list_time:.6} ns")
print(f"deque.appendleft() {TIMES} TIMES {deque_time:.6} ns  ({gain:.6}x faster)")

""" 
Accessing Random Items in a deque
"""
