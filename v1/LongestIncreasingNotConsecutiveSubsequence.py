# Find the longest increasing subsequence in the given array. Note: the elements do not
# have to be continuous.

lis      = 1     # final result
lis_dict = {}    # dic for memoization

def find_lis(arr,n):
    # base case
    assert(n >= 0)
    if n <= 1:
        return n
        
    # recursive case
    local_lis = 1   # length of LIS ending w/ arr[n-1]
    for i in xrange(1,n):
        if i in lis_dict:
            poss_prev_local_lis = lis_dict[i]
        else:
            poss_prev_local_lis = find_lis(arr,i)
            global lis_dic
            lis_dict[i] = poss_prev_local_lis           
    
        if arr[i-1] < arr[n-1]:
            local_lis = max(local_lis,poss_prev_local_lis+1)
    global lis
    lis = max(lis,local_lis)
    return local_lis

# Solution: Define f(i) to be the length of the LIS (longest increasing 
# subsequence) from arr[0,i) such that arr[i] is part of the LIS and
# arr[i] is the last element in LIS. Then, f(i) can be written as:
# f(i) = {1 + max(f(j)) s.t. j < i and arr[j] < arr[i] if such a j exists
#        {1 otherwise
# To get the LIS of the given array, return max(f(i)) where 0 < i < n.
# The above solution computes the result recursively while memoizing
# repeated computation. Time complexity is O(n^2) and space complexity
# is O(n).
# 
# Note: First, be sure to not if the interviewer is asking for increasing
# or strictly increasing. If not strictly increasing, then line 23 should be
# changed to 'if arr[i-1] <= arr[n-1]'. 
