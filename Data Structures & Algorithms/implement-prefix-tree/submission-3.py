class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        rootNode = self.root
        for w in word:
            if w not in rootNode.children:
                rootNode.children[w] = TrieNode()
            rootNode = rootNode.children[w]
        rootNode.isEnd = True

    def search(self, word: str) -> bool:
        rootNode = self.root
        for w in word:
            if w not in rootNode.children:
                return False
            rootNode = rootNode.children[w]
        return rootNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        rootNode = self.root
        for w in prefix:
            if w not in rootNode.children:
                return False
            rootNode = rootNode.children[w]
        return True      