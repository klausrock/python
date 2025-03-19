try:
    print("this gets executed first")
except:
    print("this gets executed only if there is an error")

print()

try:
    print("let's try something:")
    x = 1 / 0 # ZeroDivisionError
except:
    print("something bad happened!")

print()

def safe_divide(a, b):
    try:
        return a / b
    except:
        return "Error: 100"

print(safe_divide(1, 2))
print()

print(safe_divide(2, 0))
print()

def fibonacci(N):
    if N < 0:
        raise ValueError("N must be non-negative")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

print(fibonacci(10))
print()

print(fibonacci(-10))


