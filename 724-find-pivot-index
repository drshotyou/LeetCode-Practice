class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arrayTotal = sum(nums)
        sumLeft = 0
        for i in range(len(nums)):
            sumRight =  arrayTotal - sumLeft - nums[i]
            if(sumLeft == sumRight):
                return i
            sumLeft += nums[i]
        return -1