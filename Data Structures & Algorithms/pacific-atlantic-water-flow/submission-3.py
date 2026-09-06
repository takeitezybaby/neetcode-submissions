class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []
    
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
    
        def bfs(starts, visited):
            queue = deque(starts)
            visited.update(starts)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols 
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]):  # reverse condition
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]
        
        bfs(pacific_starts, pacific_visited)
        bfs(atlantic_starts, atlantic_visited)
        
        result = pacific_visited & atlantic_visited
        return [[r, c] for r, c in result]