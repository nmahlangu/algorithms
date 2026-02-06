import unittest

class Solution:
    def count_less_or_equal(self, matrix: list[list[int]], k: int) -> int:
        # dimensions
        l: int = len(matrix)
        w: int = len(matrix[0])

        # start in bottom left
        row: int = l - 1
        col: int = 0

        count: int = 0
        while row >= 0 and col < w:
            if matrix[row][col] <= k:
                count = count + row + 1
                col += 1
            else:
                row -= 1

        return count

    def kthSmallest(self, matrix: list[list[int]], k: int):
        # dimensions
        l: int = len(matrix)
        w: int = len(matrix[0])

        # search space
        left: int = matrix[0][0]
        right: int = matrix[l-1][w-1]

        while left < right:
            mid: int = (left + right) // 2
            num_smaller: int = self.count_less_or_equal(matrix=matrix, k=mid)

            # too small, search larger numbers
            if num_smaller < k:
                left = mid + 1

            # maybe found it, keep searching left
            else:
                right = mid

        return left

class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().kthSmallest([[ 1, 5, 9], [10,11,13], [12,13,15]], 8)
        self.assertEqual(13, actual)


if __name__ == "__main__":
    unittest.main()
