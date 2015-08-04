# You're given an array representing a histogram, where each
# element in the array is the height of a 1 unit block. Calculate
# how much rain will fall in between all of the blockes combined.

def calc_rain(arr):
	right = [0]*len(arr)
	lm = rm = -float("inf")
	rain = 0
	for i, item in enumerate(reversed(arr)):
		right[len(arr)-i-1] = rm	
		rm = max(rm,item)
	for i, item in enumerate(arr):
		lm = max(lm,item)
		max_height = min(lm,right[i])
		if max_height > item:
			rain += max_height - item
	return rain

assert(calc_rain([5,2,4,2,5]) == 7)
assert(calc_rain([-2,-4,-2]) == 2)

# Solution: Precompute the max height of any block to the left and right of every
# block. Then for each block, increment a rain counter by the (minimum
# of the left and right highest blocks for that block) - the height
# of the block, if the former difference is greater than the latter
# height. 