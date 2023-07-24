class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0): return 0
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1 not in numSet):
                curLength = 0
                while(num+curLength in numSet):
                    curLength += 1
                longest = max(curLength,longest)
        return longest
