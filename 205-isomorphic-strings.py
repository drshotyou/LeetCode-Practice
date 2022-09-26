class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {},{}
        for i in range(len(s)):
            cs,ct = s[i],t[i]
            if((cs in mapST and mapST[cs] != ct)):
                return False
            if((ct in mapTS) and mapTS[ct] != cs):
                return False
            mapST[cs] = ct
            mapTS[ct] = cs
        return True