class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target <= nums[0]):
            return 0
        elif(target > nums[len(nums)-1]):
            return len(nums)
        return binSearch(nums, target, 0, len(nums)-1)
        
def binSearch(nums, target, start, end):
    mid = start + (end - start) // 2
    if(mid>=0):
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            if(mid-1 >= 0):
                if ((nums[mid] - 1) == target) and (nums[mid-1] != target):
                    return mid
                else:
                    return binSearch(nums, target, start, mid -1)
        else:
            if(mid+1<len(nums)):
                if ((nums[mid] + 1 ) == target) and (nums[mid+1] != target):
                    return mid+1
                else:
                    return binSearch(nums,target,mid + 1, end)
           