# a and b are both sorted arrays of integers. Each contains
# n sorted integers, but a has length 2 * n, with the last n slots
# empty, and b has just n elements. This method merges the elements
# from b into a, in place, without dynamic memory allocation. Optimize
# for speed.

def inplace_merge(a,b):
    if not a:
        return b
    elif not b:
        return a
    
    a_place = len(a) - 1
    a_get = b_get = len(b) - 1

    while a_get >=0 and b_get >= 0:
        if a[a_get] > b[b_get]:
            a[a_place] = a[a_get]
            a_get -= 1
            a_place -= 1
        else:
            a[a_place] = b[b_get]
            b_get -= 1
            a_place -= 1

    while a_get >= 0:
            a[a_place] = a[a_get]
            a_get -= 1
            a_place -= 1

    while b_get >= 0:
            a[a_place] = b[b_get]
            b_get -= 1
            a_place -= 1
    return a
                
# Solution: Merge the lists together in reverse. Time complexity
# is O(n) and space complexity is O(1).
