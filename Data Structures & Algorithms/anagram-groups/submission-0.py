class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            tempStr = ''.join(sorted(s))
            ans[tempStr].append(s)
        return list(ans.values())