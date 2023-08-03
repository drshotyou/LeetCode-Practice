class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()
        l=0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            res = max(res,r-l+1)
        return res
    
# v2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        r = 0
        length = len(s)
        ans = 0
        while r < length:
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            if(r-l+1) > ans: 
                ans = r - l + 1
            r+=1
        return ans