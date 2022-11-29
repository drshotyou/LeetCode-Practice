class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}
        for i in range(len(words)): 
            wordFreq[words[i]] = 1 + wordFreq.get(words[i],0)
        
        res = sorted(wordFreq, key = lambda x: (-wordFreq[x], x))
        return res[:k]

# I like this solution
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictionary = collections.Counter(words)
        heap=[]
        for each in dictionary:
            heapq.heappush(heap,(-dictionary[each],each))
        res=[]
        for i in range(k):
            _,each=heapq.heappop(heap)
            res.append(each)
        return res