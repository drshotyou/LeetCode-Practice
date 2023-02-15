class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        cols = len(heights[0])

        pac,atl = set(),set()

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r==rows or c==cols or 
            heights[r][c] < prevHeight): return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,-1):
            dfs(rows-1,c,atl,-1)
        
        for r in range(rows):
            dfs(r,0,pac,-1)
            dfs(r,cols-1,atl,-1)
        res = []
        for cord in pac:
            if cord in atl:
                res.append(cord)
        return res