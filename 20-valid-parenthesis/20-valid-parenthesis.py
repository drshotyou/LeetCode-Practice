class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c=="{":
                stack.append(c)
            else:
                if stack and (( c == ")" and stack[-1] == "(") or ( c == "]" and stack[-1] == "[") or  (c == "}" and stack[-1] == "{")):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
        
