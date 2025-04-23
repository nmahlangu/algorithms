# Find the longest continuous subsequence of numbers in an array. The numbers
# are not streaming are all given to you at once.

def find_sequence(arr):
    longest = 0
    current = 1
    
    for i in xrange(1,len(arr)):
        if arr[i] >= arr[i-1]:
            current += 1
        else:
            longest = max(current,longest)
            current = 1

    longest = max(current, longest)
    return longest

# Solution: Do one run through and every time you see an element less than the 
# previous one, update your result to be the max of the result and the current
# length so far. Time complexity is O(n) and space complexity is O(1).


# Find the longest continuous subsequence of numbers in an array. The numbers
# are streaming and are not all given to you at once.
def find_sequence(arr_iter):
    longest = 0
    current = None    
    prev_elt = None

    while True:
        try:
            elt = arr_iter.next()
            if not current:
                current = 1
                prev_elt = elt
            elif elt >= prev_elt:
                current += 1
                prev_elt = elt
            else:
                longest = max(longest,current)
                current = 1
                prev_elt = elt
        except:
            break   

    longest = max(longest,current) if current else longest
    return longest

# Keep track of the current subsequence length and the last seen element.
# Whenever you see a new element, increment the current subsequence length
# if it's greater than the last seen element, otherwise restart the count
# of the longest subsequence. Update the last seen element as you go along.
# Time complexity is O(n) and space complexity is O(1).

