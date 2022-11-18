#v1 my solution not efficient but it's honest work
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = 'es'
        x,y = 0,0
        eL = len(matrix[0])-1
        sL = len(matrix)-1
        wL = 0
        nL = 0
        traversal = [matrix[0][0]]
        lR = False
        count = 0
        while(1):
            if (dir=='es'):
                if not(lR):
                    if(nL ==  sL):
                        lR = True
                if(x+1<=eL):
                    x+=1
                    traversal.append(matrix[y][x])
                else:
                    if(lR):
                        break
                    nL+=1
                    dir = 'ws'
            elif(dir=='ws'):
                if not(lR):
                        if(wL ==  eL ):
                            lR = True
                if(y+1<=sL):
                    y+=1
                    traversal.append(matrix[y][x])
                else:
                    dir='wn'
                    eL-=1
            elif(dir=='wn'):
                if not(lR):
                    if(nL ==  sL ):
                        lR = True
                if(x-1>=wL):
                    x-=1
                    traversal.append(matrix[y][x])
                else:
                    if(lR):
                        break
                    dir ='en'
                    sL -=1
            elif(dir=='en'):
                if not(lR):
                    if(wL ==  eL ):
                        lR = True
                if(y-1>=nL):
                    y-=1
                    traversal.append(matrix[y][x])
                else:
                    dir = 'es'
                    wL +=1
        return traversal
                
#v2 most efficient way 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traversal = []
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)

        while left < right and top < bottom:
            for i in range(left,right):
                traversal.append(matrix[top][i])
            top+=1

            for i in range(top,bottom):
                traversal.append(matrix[i][right-1])
            right -= 1
            if not(left < right and top < bottom):
                break;
            
            for i in range(right - 1, left - 1, -1):
                traversal.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                traversal.append(matrix[i][left])
            left += 1

        return traversal
