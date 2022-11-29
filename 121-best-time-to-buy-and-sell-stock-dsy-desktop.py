#V1 bad performance 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        # highest = prices[0]
        # indexHighest = 0
        profit = 0
        
        for i in range(len(prices)):
            if(prices[i]<lowest):
                lowest = prices[i]
            else:
                tempProfit = prices[i] - lowest
                if(tempProfit>profit):
                    profit = tempProfit
        return profit

#V2 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxProfit = 0
        while (right < len(prices)):
            currentProfit = prices[right] - prices[left]
            if( prices[left] < prices[right]):
                maxProfit = max(currentProfit, maxProfit)
            else:
                left = right
            right+=1
        return maxProfit

#v3 91%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        low = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                if prices[i] - low > maxProfit:
                    maxProfit = prices[i] - low
        return maxProfit
