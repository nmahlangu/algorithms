# You're given an array of strings. The first is setup() which preprocesses
# the list of words to your liking. The second is isMember(), which takes
# and word and returns whether or not the word exists in the dictionary. 
# The word passed to isMember may contain a wildcard (represented as a period),
# which match exactly one character, but any character value. Finally,
# words may contain any number of dots in any position.
#
# Examples
# trie = Trie()
# words = ["foo", "bar", "baz"]
# trie.setup(words)
# trie.is_member("foo", trie.root)      // returns True
# trie.is_member("garply", trie.root)   // returns False
# trie.is_member("f.o", trie.root)      // returns True
# trie.is_member("..", trie.root)       // returns False (there are no 2 letter words)

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

    def is_member(self, word, node):
        if not word:
            return node.is_word

        let = word[0]
        if let == '.':
            # wildcard, search each child of this node
            for child in node.children:
                if self.is_member(word[1:], node.children[child]):
                    return True
            return False
        return self.is_member(word[1:], node.children[let]) if let in node.children else False

# Solution: Implement a trie class and throw all of the words into the trie. In the
# implementation of is_member, whenever you encounter a wildcard character, recurse
# and search each child of the current node. Time complexity is O(n*k) and space complexity 
# is O(alphabet size * key length * n) = O(26 * k * n) = O(k*n).
