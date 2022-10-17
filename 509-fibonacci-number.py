class Solution:
    def fib(self, n: int) -> int:
        fibTable = table();
        return fibTable[n]
        
        
def table():
    fibTable = [0,1]
    while(len(fibTable)<=50):
        lenTable = len(fibTable)
        newVal =  fibTable[lenTable-1] + fibTable[lenTable-2]
        fibTable.append(newVal)
    # print(fibTable)
    return fibTable