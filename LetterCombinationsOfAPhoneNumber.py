# Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.

class Solution(object):
    def __init__(self):
        self.digit_dict = {1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        self.result = []        

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.letterCombinationsHelper(digits,0,"")        
        return self.result

    def letterCombinationsHelper(self,digits,digit_index,curr_str):
            # base case
            if digit_index == len(digits):
                self.result.append(curr_str)
                return

            # recursive case
            for ch in self.digit_dict[int(digits[digit_index])]:
                new_str = "".join([c for c in curr_str]) + ch
                self.letterCombinationsHelper(digits,digit_index+1,new_str)
                
# Solution: This problem screams recursion. Iterate over each letter corresponding
# to current digit, append it to the string so far, and recurse on the rest. Base case
# is when there are no more digits, in which case you store the resulting string.
