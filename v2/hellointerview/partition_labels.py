class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        if not s:
            return []

        last_index: dict[str, int] = {}
        for idx, c in enumerate(s):
            last_index[c] = idx

        result: list[int] = []
        start: int = 0
        end: int = 0

        for i, c in enumerate(s):
            end = max(end, last_index[c])

            if i == end:
                result.append(i - start + 1)
                start = i + 1

        return result