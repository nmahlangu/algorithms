# Implement atof(). Similar to atoi(), this function takes a string and 
# converts it to a float

def atof(n):
    if not n:
        return 0

    negative = True if n[0] == '-' else False
    result = 0
    seen_period = False
    divisor = 10
    numbers = [str(i) for i in xrange(10)]
    for ch in n:
        if ch == ".":
            seen_period = True
        elif ch in numbers:
            if not seen_period:
                result = (result * 10) + int(ch)
            else:
                result += float(ch) / divisor
                divisor *= 10
    return -result if negative else result

# Solution: Iterate through the string and keep a divisor initialized to 10.
# For every character, if you have not yet seen a period, the result is the 
# result multiplied by 10 plus the character cast to a string. If you have
# seen the period, add the character cast to a float divided by the divisor
# to the result, and multiply the divisor by 10. Time complexity is O(n) and
# space complexity is O(1).
