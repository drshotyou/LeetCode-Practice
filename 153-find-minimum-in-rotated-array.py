class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def binSearchMin(l,r):
            if l > r:
                return
            nonlocal min
            mid = l + (r-l) // 2
            if (nums[mid] < min):
                min = nums[mid]

            if nums[mid] > nums[r]:
                binSearchMin(mid + 1, r)
            else:
                binSearchMin(l, mid - 1)
        
        min = float('inf')
        left = 0
        right = len(nums)-1
        binSearchMin(left,right)
        return min
        