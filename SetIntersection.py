# Given 2 sets, return the intersection of them.
#
# For example,
# intersection([1,3,4,2] [5,2,4]) -> [2,4]

from sets import Set

def intersection(arr1,arr2):
	if not arr1 or not arr2:
		return []

	d = set(arr1)
	return filter(lambda x: x in d,arr2)

# Solution: Create a dictionary with all the elements in the first
# array. Then iterate over the second array and only return the
# elements that are in the dictionary.
