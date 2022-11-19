class Solution:
    def longestPalindrome(self, s: str) -> int:
        listLetters = {}
        for i in range(len(s)):
            if s[i] in listLetters:
                listLetters[s[i]]+=1
            else:
                listLetters[s[i]]=1
        palindrome = ''
        insert = 0
        middle = False
        for key in listLetters:
            if(listLetters[key]>=2):
                while(listLetters[key] != 0 and not (middle==True and listLetters[key]==1)):
                    if(listLetters[key]==1 and not middle):
                        palindrome = palindrome[:insert] + key + palindrome[insert:]
                        listLetters[key]-=1
                        middle = True
                    else:
                        palindrome = key + palindrome + key
                        listLetters[key]-=2
                        insert+=1
            elif(listLetters[key]%2==1 and middle==False):
                palindrome = palindrome[:insert] + key + palindrome[insert:]
                middle = True
        # print(palindrome)
        return len(palindrome)

#v2 bad performance best was 70% time
        sHash = {}
        for i in range(len(s)):
            if s[i] in sHash:
                sHash[s[i]] = 1 + sHash.get(s[i],0)
            else:
                sHash[s[i]] = 1
        
        ans = []
        odd = False
        for key in sHash:
            if(sHash[key] >= 2):
                while(sHash[key] >= 2):
                    ans.insert(0,key)
                    ans.append(key)
                    sHash[key] -= 2
            if (sHash[key] % 2 != 0 and not odd):
                middle = len(ans) // 2
                ans.insert(middle,key)
                sHash[key] -= 1
                odd = True
        
        # print(ans)
        return len(ans)

#v2 optimized best was 85% time
class Solution:
    def longestPalindrome(self, s: str) -> int:
        sHash = {}
        for i in range(len(s)):
            if s[i] in sHash:
                sHash[s[i]] = 1 + sHash.get(s[i],0)
            else:
                sHash[s[i]] = 1
        
        ans = ''
        odd = False
        insert = 0
        for key in sHash:
            if(sHash[key] >= 2):
                while(sHash[key] >= 2):
                    ans = key + ans + key
                    sHash[key] -= 2
                    insert+= 1
            if (sHash[key] % 2 != 0 and not odd):
                
                ans = ans[:insert] + key + ans[insert:]
                sHash[key] -= 1
                odd = True
        
        # print(ans)
        return len(ans)

#v5.2 96% time 67% space
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterFreq = Counter(s)
        length = 0
        odd = False
        for key in letterFreq:
            while letterFreq[key] > 0:
                times = letterFreq[key] // 2
                length += 2 * times
                letterFreq[key] -= 2 * times
                if(letterFreq[key] >0):
                    odd = True
                    letterFreq[key]-=1
        if(odd):
            length+=1
        return length
#V5.1 99.54% TIME 22.81% SPACE
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterFreq = Counter(s)
        length = 0
        odd = False
        for key in letterFreq:
            if letterFreq[key] % 2 == 0:
                length += letterFreq[key]
            else:
                odd = True
                length += letterFreq[key] - 1
        if(odd):
            length+=1
        return length


# All these versions rely on actually building the palindrome, but we dont really need to
#v4 best is 98.83% time 67.22% space
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = 0
        ans = 0
        for count in Counter(s).values():
            if count%2 == 0:
                ans+=count
            else:
                odd = 1
                ans += count - 1
        return ans + odd