class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        right =  1
        
        while right < len(nums):
            if(nums[left] == 0):
                if(nums[right] != 0):
                    nums[left], nums[right] = nums[right], nums[left]
                else:
                    right += 1
            else:
                left += 1
                right += 1
        
        
        
            