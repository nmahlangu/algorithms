import heapq
import unittest

class Solution:
    def kthLargest(self, nums: list[int], k: int):
        if not nums:
            return

        heap: list[int] = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0]

class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().kthLargest([5, 3, 2, 1, 4], 2)
        self.assertEqual(4, actual)


if __name__ == "__main__":
    unittest.main()

