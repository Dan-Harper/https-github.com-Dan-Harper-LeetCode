class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # pointers left, right, top, bottom
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                result.append(matrix[top][i])
            # iterate top + 1
            top += 1
            
            # get every i in the right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # get every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
        return result