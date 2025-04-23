# Implement a function to output the nth value of the fibonacci sequence

def fib(n):
    if n <= 0:
        return 0
    a = 0
    b = 1
    for i in xrange(2,n+1):
        c = a + b
        a = b
        b = c
    return b

# Solution: Time complexity is O(n), space complexity is O(1).
