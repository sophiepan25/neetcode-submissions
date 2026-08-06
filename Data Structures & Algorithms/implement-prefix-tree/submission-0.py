class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                print(f'add{c}')
                curr.children[c] = TrieNode()
                curr = curr.children[c]
            else:
                curr = curr.children[c]
        curr.endOfWord = True
            


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                print(f"current letter: {curr}, next: {c}")
                curr = curr.children[c]
        if not curr.endOfWord:
            return False
        return True

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return True

        
        