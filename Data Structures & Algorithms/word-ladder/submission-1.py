class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+'*'+word[j+1:]
                nei[pattern].append(word)
        visit = set([beginWord])
        q = deque() 
        q.append((beginWord, 1))
        while q:
            node, count = q.popleft()
            if node == endWord:
                return count
            for j in range(len(node)):
                pattern = node[:j]+'*'+node[j+1:]
                for n in nei[pattern]:
                    if n in visit:
                        continue
                    visit.add(n)
                    q.append((n, count + 1))
        return 0