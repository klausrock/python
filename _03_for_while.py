# You might notice that the meaning of range arguments is very similar 
# to the slicing syntax that we covered in Lists.

# Note that the behavior of range() is one of the differences between Python 2 and Python 3: 
# in Python 2, range() produces a list, while in Python 3, range() produces an iterable object.


for N in [2, 3, 5, 7]:
    print(N, end=' ')           # print all on same line

print()

for i in range(10):             # range from 0 to 9
    print(i, end=' ')           # print all on same line
 
print()

for N in list(range(5, 10)):    # range from 5 to 10
    print(N, end=' ')           # print all on same line

print()

for N in list(range(0, 10, 2)): # range from 0 to 10 by 2
    print(N, end=' ')           # print all on same line

print()

L = [2, 3, 5, 7]

print(L)

i = 0
while i < 10:
    print(i, end=' ')
    i += 1

print()

for n in range(20):
    # if the remainder of n / 2 is 0, skip the rest of the loop
    if n % 2 == 0:
        continue
    print(n, end=' ')

print()

a, b = 0, 1
amax = 100
L = []

while True:
    (a, b) = (b, a + b)
    if a > amax:
        break
    L.append(a)

print(L)

L = []
nmax = 30

for n in range(2, nmax):
    for factor in L:
        if n % factor == 0:
            break
    else: # no break
        L.append(n)

print(L)






