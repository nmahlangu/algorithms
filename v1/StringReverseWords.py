# Write a function that takes a string and returns the string
# with the order of the words reversed. 
#
# For example:
# "The bear ate the food" -> "food the ate bear The"

def reverse_words(s):
    if not s:
        return s

    return " ".join([word[::-1] for word in s[::-1].split(" ")])

# Solution: Reverse the string and split on the spaces. Then reverse
# each word and join all the words together with a space. Time 
# complexity is O(n) and space complexity is O(1).
