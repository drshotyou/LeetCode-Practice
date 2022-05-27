class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squaredArray = []
        left = 0
        right  =  len(nums) - 1
        while left <= right:
            if(abs(nums[left])  > abs(nums[right])):
                squaredArray.append(nums[left] ** 2)
                left += 1
            else:
                squaredArray.append(nums[right] ** 2)
                right -=1
        
        print(squaredArray)
        return squaredArray[::-1]