class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while(len(stones)>1):
            print(stones)
            if(stones[0]==stones[1]):
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] = stones[0] - stones[1]
                stones.pop(1)
            stones.sort(reverse=True)
        # print(stones)
        return stones[0] if (len(stones)>0) else 0

# using max heap but gives worse performance (leetcode results)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x*-1 for x in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            maxOne = heapq.heappop(stones)
            maxTwo = heapq.heappop(stones)
            if maxOne != maxTwo:
                if (maxOne*-1) <(maxTwo*-1):
                    heapq.heappush(stones,((maxTwo*-1)-(maxOne*-1))*-1)
                else:
                    heapq.heappush(stones,((maxOne*-1)-(maxTwo*-1))*-1)
        if stones:
            return (heapq.heappop(stones)*-1)
        else:
            return 0

        