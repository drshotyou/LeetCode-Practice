class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        length =  len(height)
        r = length - 1
        mArea = 0
        while l<r:
            curHeight = min(height[l],height[r])
            curArea = (r - l) * curHeight
            mArea = max(mArea,curArea)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return mArea