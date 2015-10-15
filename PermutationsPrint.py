# Write a function that generates the permutations of the characters
# in a string.

result = []

def gen_perm_helper(arr,word):
    if not arr:
        result.append(word)
        return

    for i in xrange(len(arr)):
        ch = arr[i]
        new_arr = [arr[j] for j in xrange(len(arr)) if i != j]
        gen_perm_helper(new_arr,word+ch)        
    

def gen_permutations(s):
    if not s:
        return []
    gen_perm_helper([ch for ch in s],"")
    return result

# Solutions: Recursively build the string up, one character at a time.
# When you have no more characters to use, store the resulting string.
# Time complexity is O(n!), where n is the number of characters in the string
# and space complexity is O(1).
