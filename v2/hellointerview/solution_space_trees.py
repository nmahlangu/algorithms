import unittest


class Solution:
    def letterCombinations(self, digits):
        result: list[str] = []
        self.backtrack(0, digits, "", result)
        return result

    def backtrack(self, idx: int, digits: str, combo: str, result: list[str]) -> None:
        if idx == len(digits):
            result.append(combo)
            return

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        letters: str = phone[digits[idx]]
        for ch in letters:
            self.backtrack(idx + 1, digits, combo + ch, result)


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().letterCombinations("23")
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], actual)


if __name__ == "__main__":
    unittest.main()
