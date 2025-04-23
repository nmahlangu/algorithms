# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two 
# lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_so_far = 0
        while l < r:
            max_so_far = max(max_so_far,(r - l) * min(height[r],height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_so_far

# Solution: have a pointer start at each end of the container and repeatedly move
# the one pointing to the shorter element towards the other. Doing so may increase
# the max area seen so far and will never decrease it. The higher one doesn't need
# to be moved since regardless if the next element is shorter or higher than the
# the previous one, the shorter element is the limiting factor for the container. 
# Each time take the max of your max area or the new area between the 2 pointers.
# Time complexity is O(n), space complexity is O(1).
