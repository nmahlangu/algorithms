from typing import *


class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int):
        base_color: int = image[sr][sc]
        self.flood_fill_helper(
            image=image, sr=sr, sc=sc, color=color, base_color=base_color
        )
        return image

    def flood_fill_helper(
        self, image: List[List[int]], sr: int, sc: int, color: int, base_color: int
    ) -> None:
        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1:
            return
        if image[sr][sc] == color:
            return
        if image[sr][sc] != base_color:
            return

        image[sr][sc] = color
        coords: list[tuple(int, int)] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in coords:
            self.flood_fill_helper(
                image=image, sr=sr + x, sc=sc + y, color=color, base_color=base_color
            )
