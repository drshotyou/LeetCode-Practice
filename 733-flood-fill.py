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
    # print(len(img),len(img[0]))
    # print(sr,sc)
    # print(img)
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