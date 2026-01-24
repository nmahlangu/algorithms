import unittest

class Solution:
    def decodeString(self, s: str):
        current_str: str = ""
        current_num: int = 0

        stack: int | str = []

        for c in s:
            if c.isdigit():
                current_num = (current_num * 10) + int(c)
            elif c.isalpha():
                current_str += c
            elif c == "[":
                stack.append(current_str)
                stack.append(current_num)
                current_str = ""
                current_num = 0
            else:
                mult: int = stack.pop()
                sub_s: str = stack.pop()
                current_str = sub_s + (mult * current_str)

        return current_str

class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().decodeString("3[a2[c]]")
        self.assertEqual("accaccacc", actual)

if __name__ == "__main__":
    unittest.main()
