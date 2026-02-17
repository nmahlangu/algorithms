"""
You have to take a total of numCourses courses, which are labeled from 0 to numCourses - 1. 
You are given a list of prerequisites pairs, where prerequisites[i] = [a, b] indicates that 
you must complete course b before course a.

Given the total number of courses and a list of prerequisite pairs, write a function to 
determine if it is possible to finish all courses.

numCourses = 3
prerequisites = [[1, 0], [2, 1]]

Output True

        # build adjacency list
        # calculate indegrees
        # enqueue nodes with indegree 0
        # continue until queue empty
        # return processed == len input
"""

from typing import *
from collections import defaultdict, deque
import unittest


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        num_courses: int = numCourses

        adj_list: dict[int, list[int]] = defaultdict(list)
        indegree: list[int] = num_courses * [0]
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] += 1

        queue: deque[int] = deque([i for i in range(num_courses) if indegree[i] == 0])

        order: list[int] = []
        while queue:
            curr: int = queue.popleft()
            order.append(curr)

            for neighbor in adj_list.get(curr, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return True if len(order) == num_courses else False


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().canFinish(3, [[1, 0], [2, 1]])
        self.assertEqual(True, actual)

    def test_example2(self):
        actual = Solution().canFinish(3, [[1, 0], [0, 1], [1, 2]])
        self.assertEqual(False, actual)


if __name__ == "__main__":
    unittest.main()
