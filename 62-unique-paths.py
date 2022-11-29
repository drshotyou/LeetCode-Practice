class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            newRow = [1]* n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1]  + row[j]
            row = newRow
        return row[0]

# v2 while i think this way is more intuitive you are looking at an inverted grid
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for j in range(m-1):
            temp = [1] * n 
            for i in range(1,n):
                temp[i] = temp[i-1] + row[i]
            row = temp
        return row[n-1] 