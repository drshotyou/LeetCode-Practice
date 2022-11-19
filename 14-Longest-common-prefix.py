#v1 not that nice to read
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if strs == [""] or strs[0] == "":
            return ""
        char = strs[0][0]
        unmatched = 0
        
        while(1):
            # print("round")
            for word in strs:
                length = len(word)
                # print('for',word,word[i])
                if i >= length:
                    # print('exceeded',i)
                    unmatched = 1
                    break
                
                elif not word[i] == char:
                    # print('not equal',i)
                    unmatched = 1
                    break
            if unmatched:
                break
            i+=1
            if(i>=len(strs[0])):
                # print(i)
                break
            char = strs[0][i]

        if i == 0:
            return ""
        else:
            return strs[0][:i]

#v2 easier to read and faster
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len) #Complexity goes to length of smallest string
        for i,ch in enumerate(shortest):
            for string in strs:
                if string[i] != ch:
                    return shortest[:i]
        return shortest