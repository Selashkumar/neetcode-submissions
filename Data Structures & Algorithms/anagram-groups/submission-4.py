class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp in obj:
                obj[temp].append(strs[i])
            else:
                obj[temp] =[strs[i]]
        return list(obj.values())






















        # ans = collections.defaultdict(list)
        # for i in strs:
        #     s  = ''.join(sorted(i))
        #     ans[s].append(i)
        # return list(ans.values())