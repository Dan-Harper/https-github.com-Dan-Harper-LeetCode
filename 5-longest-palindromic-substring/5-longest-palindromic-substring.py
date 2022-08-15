class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0
        
        for character in range(len(s)):
            left_pointer = character
            right_pointer = character
            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
                if(right_pointer - left_pointer + 1) > result_length:
                    result = s[left_pointer : right_pointer + 1]
                    result_length = right_pointer - left_pointer + 1 
                left_pointer -= 1
                right_pointer += 1
            left_pointer = character
            right_pointer = character + 1
            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
                if(right_pointer - left_pointer + 1) > result_length:
                    result = s[left_pointer : right_pointer + 1]
                    result_length = right_pointer - left_pointer + 1
                left_pointer -= 1
                right_pointer += 1
        return result