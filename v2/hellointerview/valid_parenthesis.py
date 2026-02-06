class Solution:
    def isValid(self, s: str):
        stack: list[str] = []
        mapping: dict = {"}": "{", "]": "[", ")": "("}

        for c in s:
            if c in mapping:
                if not stack or stack.pop() != mapping[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
