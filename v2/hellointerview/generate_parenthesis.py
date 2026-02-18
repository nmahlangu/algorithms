class Solution:
    def generateParenthesis(self, n: int):
        result: list[str] = []
        self.dfs(0, 0, "", n, result)
        return result

    def dfs(
        self, num_open: int, num_closed: int, path: str, n: int, result: list[str]
    ) -> None:
        if num_open + num_closed == 2 * n:
            result.append(path)
            return

        if num_open < n:
            self.dfs(num_open + 1, num_closed, path + "(", n, result)

        if num_closed < num_open:
            self.dfs(num_open, num_closed + 1, path + ")", n, result)
