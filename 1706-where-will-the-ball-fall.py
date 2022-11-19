class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        cols = len(grid[0])
        rows = len(grid)
        for ball in range(cols):
            x = ball
            for y in range(rows):
                slope = grid[y][x]
                x+=slope
                if x<0 or x>=cols or grid[y][x]!=slope:
                    ans.append(-1)
                    break
            else:
                ans.append(x)
           
        return ans
            