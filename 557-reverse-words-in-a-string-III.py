#Version 1
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        res = []
        
        for word in words:
            left = 0
            right = len(word) - 1
            
            temp = list(word)
            while left < right:
                temp[left],temp[right] = temp[right], temp[left]
                left += 1
                right -=1
                
            res.append(temp)
            res.append(" ")
        
        return "".join("".join(w) for w in res).strip()

# Version 2 using methods bit better
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = []
        
        for word in words:
            res.append(word[::-1])
            res.append(" ")
        
        s = "".join("".join(w) for w in res).strip()
        return s

