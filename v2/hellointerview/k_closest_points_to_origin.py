import heapq
import unittest
import math


class Solution:
    @staticmethod
    def dist(x1: int, y1: int, x2: int, y2: int) -> float:
        v: int = ((x1 - x2) ** 2) + ((y2 - y1) ** 2)
        return math.sqrt(v)

    def kClosest(self, points: list[list[int]], k: int) -> list[int]:
        # maxHeap
        heap: list[list[float, int, int]] = []
        h: tuple[int, int] = (0, 0)

        for p in points:
            d: float = self.dist(p[0], p[1], h[0], h[1])
            if len(heap) < k:
                heapq.heappush(heap, [-d, p[0], p[1]])
            elif -d > heap[0][0]:
                heapq.heappushpop(heap, [-d, p[0], p[1]])

        result: list[list[int, int]] = []
        for _ in range(k):
            item: list[float, int, int] = heapq.heappop(heap)
            result.append([item[1], item[2]])

        return result


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().kClosest([[3, 4], [2, 2], [1, 1], [0, 0], [5, 5]], 3)
        self.assertEqual([[2, 2], [1, 1], [0, 0]], actual)


if __name__ == "__main__":
    unittest.main()
