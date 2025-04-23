# Consider the binary representation of 2 numbers. The Hamming distance
# between these 2 numbers is defined as the number of bits at which these
# numbers differ. Given n integers, calculate the sum of Hamming distances
# for all pairs of numbers.
#
# For example,
# [21,11] -> [0b10101, 0b1011] = 4

def hamm_dist(arr):
    if not arr:
        return 0

    max_bin_len = 32    # max size for an int is 4 bytes
    count = 0
    for i in xrange(max_bin_len):
        ones = zeroes = 0
        for j in range(len(arr)):
            if arr[j] & 1:
                ones += 1
            else:
                zeroes += 1
            arr[j] >>= 1
        count += (ones * zeroes)
    return count

# Solution: Iterate from the 1st to the 32nd bit. In each step of this
# iteration, iterate through each number of the array, keeping track 
# of the number of 0 and number of 1 bits in the least significant
# bit. Increment the overall count by the number of 0s times the number
# of 1s, since for each 0 you want to add 1 to your overall count. Right
# shift every element of the array by 1 every time you see it here since
# you no longer need the least significant bit. Time complexity is
# O(nlog(m)), where is the number of elements and m is the largest number,
# and space complexity is O(1).
