class Tries:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Tries()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = Tries()
                cur = cur.children[c]
            cur.isEnd = True
        res, visit = set(), set()
        rows, cols =len(board), len(board[0])
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or (r, c) in visit or r == rows or c == cols or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, '')
        return list(res)