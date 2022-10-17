class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 0
        for i in range(n):
            temp = one
            one = one + two
            two = temp
        return one