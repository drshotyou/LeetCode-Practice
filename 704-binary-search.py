class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(nums[len(nums)-1] < target):
            return -1
        else:
            return binSearch(nums,target,0,len(nums))
        
def binSearch(nums,target,left,right):
    if(right-left+1) <= 0:
        return -1;
    else:
        mid = left + (right - left) // 2;
        if(nums[mid]==target):
            return mid
        elif(target < nums[mid]):
            return binSearch(nums,target,left,mid-1)
        else:
            return binSearch(nums,target,mid+1,right)


#Time complexity: O(logN)
#Space complexity: O(logN)

#v2 exit condition differs
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binSearch(nums,target,0,len(nums)-1)

def binSearch(nums,target,left,right):
    if not left <= right:
        return -1
    mid = left + (right - left) // 2
    if(nums[mid]==target):
        return mid
    elif(nums[mid]<target):
        return binSearch(nums,target,mid+1,right)
    else:
        return binSearch(nums,target,left,mid-1)