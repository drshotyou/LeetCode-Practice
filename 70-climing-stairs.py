class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 0
        for i in range(n):
            temp = one
            one = one + two
            two = temp
        return one

# a bit faster
class Solution:
    def climbStairs(self, n: int) -> int:
       
        if n in [1,2]:
            return n
       
        first = 1
        second = 2
        for i in range(3,n+1):
            first,second = second,first+second
        return second