class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {}
        best = {i: float('inf') for i in range(1, n + 1)}  # tracks best known so far, even unfinalized
        best[k] = 0
        pq = [(0, k)]
        
        while pq:
            d, node = heapq.heappop(pq)
            
            if node in dist:
                continue
            dist[node] = d
            
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < best[neighbor]:   # <-- your check
                    best[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        if len(dist) != n:
            return -1
        return max(dist.values())