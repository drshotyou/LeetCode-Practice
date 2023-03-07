class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) return ""
        countT = Collections.Counter(t)
        window = {}
        l = 0
        res,resLen = [-1,-1], float(inf)
        have,need = 0,len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c)
            if c in countT and window[c] == countT[c]:
                have+=1

            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res=[l,r]
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float(inf) else ""
