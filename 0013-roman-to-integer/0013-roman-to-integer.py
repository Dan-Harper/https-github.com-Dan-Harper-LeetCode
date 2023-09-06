class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M": 1000}
        
        result = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                # if i + 1 is in bounds and value is less than next value
                result -= roman[s[i]]
                # subtracts from result
            else:
                # add
                result += roman[s[i]]
        return result