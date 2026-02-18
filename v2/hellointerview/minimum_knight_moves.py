from collections import deque


class Solution:
    def minimum_knight_moves(self, x: int, y: int):
        queue: deque[tuple[int, int, int]] = deque([(0, 0)])
        directions: list[tuple[int, int]] = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]
        visited: set[tuple[int, int]] = set()
        lvl_moves: int = 0

        while queue:
            lvl_len: int = len(queue)

            for _ in range(lvl_len):
                row, col = queue.popleft()

                if row == x and col == y:
                    return lvl_moves

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((row, col))

            lvl_moves += 1

        return -1
