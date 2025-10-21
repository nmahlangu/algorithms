
from typing import *
from collections import deque

"""
- Backtrack and store every path as you build up each result
- tc: O(n*4^n), n=num of letters in input
- sc: O(n) extra space, O(n*4^n) where n=num of letters in input
"""

class Solution:

    digit_to_letters: Dict[str, str] = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        s = deque()
        s.appendleft((0, ""))
        combos = []

        while len(s) > 0:
            index, result = s.popleft()

            if index == len(digits):
                combos.append(result)
            else:
                for c in self.digit_to_letters[digits[index]]:
                    s.appendleft((index+1, result + c))

        return combos

s = Solution()

assert list(sorted(s.letterCombinations("34"))) == ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
