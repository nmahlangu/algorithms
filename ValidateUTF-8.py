# Given a array of encoded bytes (represented as strings in the problem), 
# write a function that returns true iff the bytes represent a valid UTF-8 
# encoded string (note: the string can have more than one UTF-8 character).
#
# For example,
# ["01100010"]                         -> True
# ["11100100", "10110100", "10000110"] -> True

# returns the number of leading ones in string
def leading_ones(byte):
    ones = 0
    for b in byte:
        if b == "1":
            ones += 1
        else:
            break
    return ones

def valid_utf8(bytes):
    if not input:
        return False

    bytes_left = 0
    for byte in bytes:
        l_ones = leading_ones(byte)
        if bytes_left <= 0:
            if l_ones == 1:
                return False
            bytes_left = l_ones - 1
        else:
            if l_ones != 1:
                return False
            bytes_left -= 1
    
    return bytes_left <= 0

# Solution: Edge cases to be weary about is a lack of a continuation
# byte, an incorrect continuation byte, and too many continuation
# bytes. Iterate through all the bytes, keeping track of how many bytes
# are left until the next encoded character. If you ever encounter
# a continuation byte when you shouldn't, return False. If you ever
# encounter a different byte than a continuation character when you
# shouldn't, return False. Time complexity is O(n) and space complexity
# is O(1).
