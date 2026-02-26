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
    
    def search(self, word: str) -> bool:
        """
        Search the trie for the given word.

        Returns True if the word exists in the trie, False otherwise
        """
        node: TrieNode = self.root

        for c in word:
            if c not in node.children:
                return False

            node = node.children[c]

        return node.isEndOfWord

    def delete(self, word: str) -> None:
        """
        Deletes the given the word from the Trie.

        Returns None.
        """
        self.delete_helper(self.root, word, 0)
        return

    # traverses down trie to find node at end of word
    # marks node's isEndofWord to False
    # recursively deletes on the way back up (current node
    # is not an end and has no children)
    def delete_helper(self, node: TrieNode, word: str, index: int) -> bool:
        # base case
        if index == len(word):
            node.isEndOfWord = False
            return len(node.children) == 0

        # recursive
        ch: str = word[index]
        if ch not in node.children:
            return False

        ch_node: TrieNode = node.children[ch]
        should_delete: bool = self.delete_helper(ch_node, word, index + 1)
        if should_delete:
            del node.children[ch]

        return not node.isEndOfWord and len(node.children) == 0


    def trie(self, initialWords, commands):
        # === DO NOT MODIFY ===
        self.create_trie(initialWords)

        output = []
        for command, word in commands:
            if command == "search":
                output.append(self.search(word))
            elif command == "delete":
                self.delete(word)
        return output