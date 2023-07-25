class Solution:
    # two pointers but slow
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            print(s[left], s[left].isalnum(), s[right], s[right].isalnum())
            if(s[left].isalnum() and s[right].isalnum()):
                if(s[left].lower()!=s[right].lower()):
                    return False
                else:
                    left+=1
                    right-=1
            if(not s[left].isalnum()):
                left+=1
            if(not s[right].isalnum()):
                right-=1
        return True

        # fast 
        def isPalindrome(self,s:str)  -> bool:
            s = [c.lower() for c in s if c.isalnum()]
            # print(s)
            if(s == s[::-1]):
                return True
            return False