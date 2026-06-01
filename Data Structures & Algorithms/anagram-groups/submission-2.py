class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for i in strs:
            s  = ''.join(sorted(i))
            ans[s].append(i)
        return list(ans.values())