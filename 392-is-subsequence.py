class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if(len(s)>0):
            for i in range(len(t)):
                if(index>=len(s)):
                    break
                else:
                    print(s[index], ' ', t[i])
                    if(s[index]==t[i]):
                        print('found')
                        index+=1
        print(index, ' ', len(s))
        if(index == len(s)):  
            return True
        else:
            return False
                

#v2 96%

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)==0): return True
        if len(s) > len(t):
            return False
        lettersFound = 0

        for i in range(len(t)):
            if(lettersFound>=len(s)):
                break
            if(t[i]==s[lettersFound]):
                lettersFound +=1
        if lettersFound == len(s):
            return True
        else:
            return False