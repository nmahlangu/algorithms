class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def create_trie(self, words):
        # === DO NOT MODIFY ===
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        # === DO NOT MODIFY ===
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
    
    def prefix(self, word: str) -> list[str]:
        """
        Return a list of all words in the trie that start with the given prefix.
        """
        # fetch node after prefix
        node: TrieNode = self.root
        for ch in word:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result: list[str] = []

        self.dfs(node, word, result)
        return result

    def dfs(self, node: TrieNode, path: str, result: list[str]) -> None:
        if node.isEndOfWord:
            result.append(path)

        for ch, ch_node in node.children.items():
            self.dfs(ch_node, path + ch, result)

        return

    def trie(self, words, prefix):
        # === DO NOT MODIFY ===
        self.create_trie(words)
        return self.prefix(prefix)