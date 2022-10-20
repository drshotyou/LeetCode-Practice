#O(26*n) solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sCount = {}
        l = 0
        r = 0
        maxC = 0
        res = 0
        while (r < len(s)):
            # print(sCount)
            sCount[s[r]] = 1 + sCount.get(s[r],0)
            for key in sCount:
                if(sCount[key] > maxC):
                    maxC = sCount[key]
            windowLenReps = (r-l)+1 
            if(windowLenReps - maxC <= k ):
                res = windowLenReps
                if(r == len(s)-1):
                    break
            else:
                sCount[s[l]] = sCount.get(s[l],0) - 1
                l += 1
            r+=1
        return res
        
#O(n) solution
