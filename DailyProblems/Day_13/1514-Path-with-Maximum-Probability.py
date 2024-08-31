import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        
        pq = [(-1.0, start_node)]
        
        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob
            
            if node == end_node:
                return prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0.0
