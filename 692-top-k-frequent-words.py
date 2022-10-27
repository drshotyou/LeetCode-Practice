class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}
        for i in range(len(words)): 
            wordFreq[words[i]] = 1 + wordFreq.get(words[i],0)
        
        res = sorted(wordFreq, key = lambda x: (-wordFreq[x], x))
        return res[:k]