class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        # iterate through rows except last row
        for i in range(m - 1):
            # for each row computer a new row
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                # iterate through every column
                # except right-most column
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]