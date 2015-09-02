# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string text, int nRows);
# Convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Naive_Solution:
    def convert(self, s, numRows): 
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        buckets = [[] for i in range(numRows)]
        bucket_index = 0
        increment = True
        for c in s:
            if bucket_index == numRows:
                bucket_index -= 2
                increment = False
            elif bucket_index == -1:
                bucket_index += 2
                increment = True
            buckets[bucket_index].append(c)
            bucket_index = bucket_index + 1 if increment else bucket_index - 1            
	return reduce(lambda acc, elt: acc+"".join(elt),buckets,"")

# Naive Solution: Build up the zigzag character matrix using a 2D array, then join together
# each row of the 2D array as a string and return all the strings concatenated. Time and space
# complexity are both O(n).

class Solution:
	def convert(self, s, numRows):	
		if numRows == 1:
			return s
		num_buckets = numRows + numRows - 2
		new_s = ""
		for i in range(numRows):
			curr = i
			while curr < len(s):
				new_s += s[curr] # char in full column
				curr += num_buckets
				if (i > 0) and (i < numRows - 1) and (curr - i - i < len(s)):
					new_s += s[curr - i - i] # char in next not-full column
		return new_s

# Solution: Generate the final string by computing the indices you need ahead of time. Imagine each
# possible position a character can be in in the zig zag as a different bucket (e.g. if there's 4
# rows there are 6 buckets given by 2*numRows - 2). For each row of the zig zag, you can get the next
# character in a full column by adding the number of buckets. To get the char in a not full column
# that was skipped over, subtract twice the offset of the current row from the first one from the next
# character and append that first. Time complexity is O(n); space complexity is O(1).
