class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword= False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word->str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children
        return cur.endofword
    
    def  startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children
        return True
