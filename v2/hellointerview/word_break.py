from typing import *
import unittest

"""
1) recurrence relation
The string S ending at index i can be segmented if S[j:i+1] is a valid word and S[:j]
can be segmented, such that j < i. If S[:j] doesn't exist, return True

Claude:   In plain English: "The first i characters can be segmented if there's
some split point j where the first j characters can be segmented AND
the remaining substring from j to i is a dictionary word."
"""


class Solution:
    def word_break_bu(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        dp: list[bool] = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_hello_interview(self):
        self.assertTrue(self.s.word_break_bu("hellointerview", ["hello", "interview"]))

    def test_catsandog(self):
        self.assertFalse(
            self.s.word_break_bu("catsandog", ["cats", "dog", "sand", "and", "cat"])
        )

    def test_leetcode(self):
        self.assertTrue(self.s.word_break_bu("leetcode", ["leet", "code"]))

    def test_applepenapple(self):
        self.assertTrue(self.s.word_break_bu("applepenapple", ["apple", "pen"]))

    def test_single_char_match(self):
        self.assertTrue(self.s.word_break_bu("a", ["a"]))

    def test_single_char_no_match(self):
        self.assertFalse(self.s.word_break_bu("b", ["a"]))

    def test_reuse_word(self):
        self.assertTrue(self.s.word_break_bu("aaaa", ["a", "aa"]))

    def test_no_valid_segmentation(self):
        self.assertFalse(self.s.word_break_bu("catsdog", ["cats", "og"]))

    def test_whole_string_is_one_word(self):
        self.assertTrue(self.s.word_break_bu("banana", ["banana"]))

    def test_overlapping_words(self):
        self.assertTrue(
            self.s.word_break_bu(
                "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
            )
        )


if __name__ == "__main__":
    unittest.main()
