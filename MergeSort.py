# Implement Mergesort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
        left = arr[:mid]
        right = arr[mid:]

        # recursively sort each half
        merge_sort(left)
        merge_sort(right)

        # combine sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Solution: Recursively sort each half, then merge the sorted halves. There
# are (log(n)) recursive splits and merging takes O(n), so overall the time
# complexity is O(nlog(n)) and space complexity is O(1).
