class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            if target - numbers[i]  in seen:
                return [seen[target - numbers[i]]+1, i+1]
            seen[numbers[i]] = i
        return []





















        # l,r=0,len(numbers) - 1
        # while l < r:
        #     curSum = numbers[l] + numbers[r]
        #     if curSum < target:
        #         l +=1
        #     elif curSum > target:
        #         r -=1
        #     else:
        #         return [l+1,r+1]
        # return []