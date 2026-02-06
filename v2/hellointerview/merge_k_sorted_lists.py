import heapq
import unittest

class Solution:
    def mergeKLists(self, lists: list[list[int]]):
        # item will be (val, idx of list)
        heap: list[tuple[int,int]] = []
        
        # throw heads of all lists into heap 
        for i in range(len(lists)):
            if len(lists[i]) == 0:
                continue

            heapq.heappush(heap, (lists[i][0], i))
            lists[i] = lists[i][1:]

        result: list[int] = []
        while len(heap) > 0:
            elt, idx = heapq.heappop(heap)
            result.append(elt)

            if len(lists[idx]) > 0:
                heapq.heappush(heap, (lists[idx][0], idx))
                lists[idx] = lists[idx][1:]

        return result

class TestSolution(unittest.TestCase):
    def test1(self):
        actual = Solution().mergeKLists(lists=[[3,4,6],[2,3,5],[-1,6]])
        self.assertEqual(actual, [-1,2,3,3,4,5,6,6])

if __name__ == '__main__':
    unittest.main()


        