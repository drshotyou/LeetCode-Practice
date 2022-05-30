class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums = reverse(nums, 0, len(nums) - 1)
        nums = reverse(nums, 0, k-1)
        nums = reverse(nums, k, len(nums) - 1)
            
            
def reverse(nums,left,right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1
    return nums