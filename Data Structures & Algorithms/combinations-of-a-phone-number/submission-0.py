class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        numMap = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        for dig in digits:
            tempVal = []
            for numVal in numMap[dig]:
                for i in res:
                    tempVal.append(i + numVal)
            res = tempVal
        return res