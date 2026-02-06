import heapq
import unittest

class Solution:
    def kClosest(self, nums: list[int], k: int, target: int):
        # items are (dist, elt)
        maxHeap: list[int,int] = []

        for n in nums:
            d: int = abs(n - target)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, [-d, n])
            elif d < -maxHeap[0][0]:
                heapq.heappushpop(maxHeap, [-d, n])

        return list(sorted([heapq.heappop(maxHeap)[1] for _ in range(k)]))

class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().kClosest(nums=[-1, 0, 1, 4, 6], k=3, target=1)
        self.assertEqual([-1, 0, 1], actual)

if __name__ == "__main__":
    unittest.main()