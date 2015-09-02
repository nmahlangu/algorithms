class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self,nums1,nums2):
    	m = len(nums1) + len(nums2)
    	if m % 2 == 1:
    		return self.kth(nums1,nums2,m/2)
    	else:
    		return (self.kth(nums1,nums2,(m/2)-1) + self.kth(nums1,nums2,m/2) / 2

    def kth(self,a,b,k):
    	if not a:
    		return b[k]
    	if not b:
    		return a[k]

    	midA,midB = len(a)/2,len(b)/2

    	if midA + midB < k:
    		if a[midA] > b[midB]:
    			return self.kth(a,b[midB+1:],k-midB-1)
    		else:
    			return self.kth(a[midA+1:],b,k-midA-1)
    	else:
    		if a[midA] > b[midB]:
    			return self.kth(a[:midA],b,k)
    		else:
    			return self.kth(a,b[:midB],k)

# Solution: generalize this question to "kth element in 2 sorted arrays"
#
# Define the following sections:
# [a_0,a_1,a_2...a_m/2,a_m/2+1...a_m-2,a_m-1] for A
# |---- Section 1 ----||---- Section 2 ----|
#
# [b_0,b_1,b_2...b_n/2,b_n/2+1...b_n-2,b_n-1] for B
# |---- Section 3 ----||---- Section 4 ----|
#
# Case: m/2 + n/2 < k, meaning kth element can only be located in Section 2 or 4 because...
# 	- Subcase: a[m/2] > b[n/2], then b[n/2] must be < kth element and kth element can't be in Section 3
# 		* e.g. A = [6,7,8,9,10] | B = [1,2,3,4,5]  | m = len(A) = 5 | n = len(B) = 5 | k = 5
#  			   8 > 3 so 3 < kth element so kth element can't be in section 3 
#   - Subcase: a[m/2] < b[n/2], then a[n/2] must be < kth element and kth element can't be in Section 1
#       * e.g. A = [1,2,3,4,5]  | B = [6,7,8,9,10] | m = len(A) = 5 | n = len(B) = 5 | k =  5
#              3 < 8 so 3 < kth element so kth element can't be in Section 1
#
# Case: m/2 + n/2 > k, meaning kth element can only be located in Section 1 or 3 because...
# 	- Subcase: a[m/2] > b[n/2], then a[m/2] must be > kth element and kth element can't be in Section 2
#		* e.g. A = [6,7,8,9,10] | B = [3,4,5] | m = len(A) = 3 | n = len(B) = 5 | k = 2
#			   8 > 4 so 8 > kth element so kth element can't be in section 2
#   - Subcase: a[m/2] < b[n/2], then b[m/2] must be > kth element and kth element can't be in Section 4
#		* e.g. A = [3,4,5] | B = [6,7,8,9,10] | m = len(A) = 3 | n = len(B) = 5 | k = 2
#			   4 < 8 so 8 > kth element so kth element can't be in section 4
