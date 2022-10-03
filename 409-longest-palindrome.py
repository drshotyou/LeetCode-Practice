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