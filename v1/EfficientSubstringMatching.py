# Given two strings s1 and s2, write a function that prints all the occurrences
# of s2 in s1. Assume only ascii values, of which there are 256.
#
# For example:
# "This is a test", "test" -> 10
# "AABAACAADAABAAABAA", "AABA" -> 0, 9, 13

# constants
prime = 211
alpha_len = 256

def rabin_karp(s1,s2):
    if len(s1) < len(s2):
        return False

    n = len(s1)
    m = len(s2)
    s1_hash = 0                     # rolling hash of s1 substring     
    s2_hash = 0                     # hash of s2
    mult = alpha_len ** (m - 1)     # used for removing first digit

    # calculate hash value of first s1 substring
    for i in xrange(m):
        s1_hash = ((alpha_len * s1_hash) + ord(s1[i])) % prime
        s2_hash = ((alpha_len * s2_hash) + ord(s2[i])) % prime

    # slide pattern over text one by one
    for i in xrange(n-m+1):
        if s1_hash == s2_hash:      # check hash values
            if s1[i:i+m] == s2:     # check for string equality
                print i

        # recalculate rolling hash for next substring
        if i < (n - m):
            s1_hash = abs((alpha_len * (s1_hash - (ord(s1[i]) * mult)) + ord(s1[i+m])) % prime)

# Solutions:
#
# Naive Algorithm: Repeatedly slide s2 over s1 one by one and check for a match. Assuming 
#                  length of s1 is n and length of s2 is m, time complexity is O(nm) and 
#                  space complexity is O(1).
#
# Rabin-Karp Algorithm: (Implemented above) Like the naive algorithm, Rabin-Karp also slides 
#                       s2 over s1 one by one. However, Rabin-Karp compares the hash value 
#                       of s2 with the hash value of the current substring of s1 and only if 
#                       they match are the strings actually compared. Using a rolling hash, 
#                       the best and average case running time of Rabin-Karp is O(n+m), however 
#                       worst case is still O(nm). The space complexity is O(1). Note: The
#                       hash function used above is the sum of the string where the string
#                       is a base 256 number.
