class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        first = cost[0]
        second = cost[1]
        if(length <= 2):
            return  first if first < second else second
        for i in range(2,length):
            current = cost[i] + (first if first < second else second)
            first = second
            second = current
        return first if first < second else second
        
    