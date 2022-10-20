#O(n^2) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for (j) in range(i+1,len(nums)):
                # print(i,j)
                if(nums[i]+nums[j]==target):
                    # print(nums[i],nums[j])
                    print(i,j)
                    return i,j

#O(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in count):
                return count[diff],i
            count[nums[i]]=i
        return