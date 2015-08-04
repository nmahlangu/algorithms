class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    
    def getMedian(self, arr):
        if len(arr) % 2 != 0:
            return arr[len(arr)/2]
        else:
            return (arr[len(arr)/2] + arr[(len(arr)/2)-1]) / 2.

    def findMedianSortedArrays(self,nums1,nums2):
        if len(nums1) <= 2 or len(nums2) <= 2:
            # nums1 is always of length 2
            if len(nums2) == 2:
                nums1,nums2 = nums2,nums1
            # do adjustments here instead
            for elt in nums1:
                nums2.append(elt)
            nums2.sort()
            return self.getMedian(nums2)

        else:
            nums1_med = self.getMedian(nums1)
            nums2_med = self.getMedian(nums2)
            # nums1 is always the one w/ smaller median
            if nums2_med < nums1_med:
                nums1,nums2 = nums2,nums1
                nums1_med,nums2_med = nums2_med,nums1_med
            elif nums1_med == nums2_med:
                return nums1_med
            num_to_del = len(nums1)/2
            new_nums1 = nums1[len(nums1)/2:]
            new_nums2 = nums2[:len(nums2)-num_to_del]
            return self.findMedianSortedArrays(new_nums1,new_nums2)

# print Solution().findMedianSortedArrays([1,7,11],[2,4,5,7,9,12,13,15,19,21,255,260,390])
# print Solution().findMedianSortedArrays([1],[])
print Solution().findMedianSortedArrays([1,2,3],[4,5,6])