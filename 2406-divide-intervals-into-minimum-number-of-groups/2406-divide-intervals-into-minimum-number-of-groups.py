import heapq

class Solution:
    def minGroups(self, intervals):
        intervals.sort()
        heap = []
        
        for interval in intervals:
            if heap and heap[0] < interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        
        return len(heap)