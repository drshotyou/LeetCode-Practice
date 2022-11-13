class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        
        for i in range(len(s)):
            if(s[i]!='#'):
                stackS.append(s[i])
            else:
                if(len(stackS)>0):
                    stackS.pop()
        # print(stackS)
        for j in range(len(t)):
            if(t[j]!='#'):
                stackT.append(t[j])
            else:
                if(len(stackT)>0):
                    stackT.pop()
        # print(stackT)
        if(len(stackS) != len(stackT)):
            return False
        for i in range(len(stackS)):
            if(stackS[i] != stackT[i]):
                return False;
        return True
            

#v2 done in one loop
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        longest = None
        if(len(s)>len(t)):
            longest = len(s)
        else:
            longest = len(t)
        sStack = []
        tStack = []
        for i in range(longest):
            if(i < len(s)):
                if(s[i]!='#'):
                    sStack.append(s[i])
                else:
                    if(sStack):
                        sStack.pop()
            if(i < len(t)):
                if(t[i]!='#'):
                    tStack.append(t[i])
                else:
                    if(tStack):
                        tStack.pop()

        if(sStack == tStack): return True
        else : return False