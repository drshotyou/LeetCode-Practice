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
            