class Solution:
    def calculate(self, s:str)->int:
            stack, cur, op = [], 0, "+"
            s = s.replace(" ","")
            for i in s + "t":
                if i.isdigit():
                    cur = cur*10 + int(i)
                else:
                    if op == "+":
                         stack.append(cur)
                    elif op == "-":
                         stack.append(-cur)
                    elif op == "*":
                        stack.append(stack.pop() * cur)
                    elif op == "/":
                         stack.append(int(stack.pop() / cur))
                    cur,op = 0,i
            return sum(stack)