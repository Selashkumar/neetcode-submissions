class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] != numbers[i] and target - numbers[i] in numbers:
                temp = i + 1
                tar = target - numbers[i] 
                while numbers[temp] != tar:
                    temp+=1
                return [i + 1,temp + 1]