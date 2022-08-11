class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {}
        
        for index, number in enumerate(nums):
            difference = target - number
            if difference in previousMap:
                return [previousMap[difference], index]
            previousMap[number] = index
        return