# Write a program that multiplies to integers (represented as strings) of an
# arbitrary size.

def mult(num1,num2):
    n = len(num1)
    m = len(num2)
    result = [0]* (2 * max(n,m))

    # compute sum of all columns
    for i in xrange(n-1,-1,-1):
        carry = 0
        for j in xrange(m-1,-1,-1):
            num = (int(num1[i]) * int(num2[j])) + carry
            carry = num / 10
            value = num % 10
            result[(n-1-i) + (m-1-j)] += value
        if carry > 0:
            result[m+(n-1-i)] = carry

    # fix carrying
    carry = 0
    for i in xrange(len(result)):
        new_val = result[i] + carry
        carry = new_val / 10
        result[i] = new_val % 10        

    return "".join(reversed(map(lambda x: str(x),result))).lstrip("0")

# Store the result's least significant bit first. For each number in the first number
# (iterated over backwards), for each number in the second number (iterated over backwards)
# calculate the product of multiplying the two numbers in question plus the left over carry. 
# The carry then becomes the aforementioned sum divided by 10, and the value to add at the
# appropriate index is the aforementioned sum. Once you've iterated through both numbers,
# iterate through the array once more fixing the sums that are more than 10 by carrying.
# Time complexity is O(n*m), where n is the length of the first number and m is the length
# of the second number, and space complexity is O(n+m).
