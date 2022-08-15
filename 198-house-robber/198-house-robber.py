class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        
        for house in nums:
            temporary = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = temporary
        return rob2