class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if(image[sr][sc]!=color):
            print('filling')
            image = replaceColor(image,sr,sc,color,image[sr][sc])
            image[sr][sc]=color
        return image
#               -sr,sc
#     sr,-sc     sr,sc     sr,+sc
#               +sr,sc
        
def replaceColor(img,sr,sc,color,ogColor):
    if sr-1 >= 0:
        if(img[sr-1][sc]!=color and img[sr-1][sc]==ogColor):
            # print('-sr,sc')
            img[sr-1][sc] = color
            img = replaceColor(img,sr-1,sc,color,ogColor)
    if sc-1 >= 0:
        if(img[sr][sc-1]!=color and img[sr][sc-1]==ogColor):
            # print('sr,-sc')
            img[sr][sc-1]=color
            img = replaceColor(img,sr,sc-1,color,ogColor)
    if sr+1 < len(img):
        if(img[sr+1][sc]!=color and img[sr+1][sc]==ogColor):
            # print('+sr,sc')
            img[sr+1][sc] = color
            img = replaceColor(img,sr+1,sc,color,ogColor)
    if sc+1 < len(img[0]):
        print('sc+1')
        
        if(img[sr][sc+1]!=color and img[sr][sc+1]==ogColor):
            img[sr][sc+1]=color
            # print('sr,+sc')
            img = replaceColor(img,sr,sc+1,color,ogColor)
    return img

#V2 Better than 91%, checks all conditions first, then runs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogColor = image[sr][sc]
        
        def flood_fill(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == color: return
            if image[x][y] != ogColor: return
            
            image[x][y] = color
            
            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)
        
        flood_fill(sr, sc)
        return image