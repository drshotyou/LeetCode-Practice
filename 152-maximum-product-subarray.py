class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res  = max(nums) #0 -> [-1]
        res = float(-inf)
        curMin, curMax = 1,1
        for n in nums:
            tmp = curMax * n
            curMax = max(n,n*curMax, n*curMin)
            curMin = min(n, tmp, n*curMin)
            res = max(res,curMax)
        return res