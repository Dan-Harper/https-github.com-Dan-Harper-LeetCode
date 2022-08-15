class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = nums[0]
        currentSum = 0
        
        for number in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += number
            maxSubArray = max(maxSubArray, currentSum)
        return maxSubArray