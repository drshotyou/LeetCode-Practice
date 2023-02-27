class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time O(n * m) m = n (wait time)
        
        # queue to process task if it is the time to process int
        # maxheap of tasks
        count  = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        # --------------
        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time +=1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 # get current most frequent task
                if cnt: # if still needs to be done again
                    q.append([cnt,time + n])    # add it to the queue
            if q and q[0][1] == time:   #if q has elements and element at top of queue has iddleTime equal to currentTime
                heapq.heappush(maxHeap,q.popleft()[0]) #pop that element from the queue and push it into the maxHeap
        return time

                    

       
