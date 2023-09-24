class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []
        # depth first search
        def dfs(i):
            # recursive function so check base case first
            # if i is out of bounds
            if i >= len(s):
                result.append(partition.copy())
                return
            # if we have not reached the last index
            # iterate through every other character
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    partition.append(s[i:j + 1])
                    dfs(j + 1)
                    partition.pop()
        dfs(0)
        return result
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True