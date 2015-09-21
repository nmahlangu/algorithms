class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word, node):
        if not word:
            node.is_word = True
            return

        let = word[0]
        if let in node.children:
            self.insert(word[1:], node.children[let])
        else:
            node.children[let] = Node()
            self.insert(word[1:], node.children[let])

    def setup(self, words):
        for word in words:
            self.insert(word, self.root)
    
    def print_trie(self, s, node):
        if node.is_word:
            print s

        for c in node.children:
            self.print_trie(s + c, node.children[c])

    def is_member(self, word, node):
        if not word:
            # if we're at the end of the word
            return node.is_word

        let = word[0]
        if let == '*':
            # wildcard, search each child of this node
            for child in node.children:
                if self.is_member(word[1:], node.children[child]):
                    return True
            return False

        if let in node.children:
            return self.is_member(word[1:], node.children[let])
        else:
            return False    

trie = Trie()
words = ["foo", "bar", "baz"]
trie.setup(words)
print trie.is_member("foo", trie.root)
print trie.is_member("garply", trie.root)
print trie.is_member("f*o", trie.root)
print trie.is_member("**", trie.root)
