class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def depth_first_search(i):
            # case where out of bounds
            if i >= len(nums):
                # subset will be modified
                result.append(subset.copy())
                return
            
            # decision to include nums[index]
            subset.append(nums[i])
            depth_first_search(i + 1)
            
            # decision NOT to include nums[index]
            subset.pop()
            depth_first_search(i + 1)
            
        depth_first_search(0)
        return result