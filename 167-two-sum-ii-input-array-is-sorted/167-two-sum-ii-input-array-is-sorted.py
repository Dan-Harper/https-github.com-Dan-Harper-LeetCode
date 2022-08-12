class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers) - 1
        
        while left_pointer < right_pointer:
            current_sum = numbers[left_pointer] + numbers[right_pointer]
            
            if current_sum < target:
                left_pointer += 1
            
            if current_sum > target:
                right_pointer -= 1 
            
            if current_sum == target:
                return [left_pointer + 1, right_pointer + 1]