# Given a list of words, return a list of lists where each list
# is a group of anagrams. Do not include words that don't have any
# anagrams in the final result (aka don't include lists of length 1).
# 
# For example, for: 
# ["cat", "act", "tac", "quiet", "quite", "sandwich"]
#
# return:
# [["cat", "act", "tac"], ["quiet", "quite"]]

def find_anagrams(arr):
    if not arr:
        return []

    result_dict = {}
    for word in arr:
        sorted_word = "".join(sorted(word))
        result_dict.setdefault(sorted_word,[])
        result_dict[sorted_word].append(word)

    return filter(lambda x: len(x) > 1, result_dict.values())

# Solution: Create a dictionary where the key is a sorted word
# and the value is an array of words that when sorted, map to
# the key. Return the dictionary values, filtering out arrays
# that have a length < 1. Assuming there are n words and the 
# length of the longest word is m, time complexity is O(nmlog(m))
# and space complexity is O(n).
