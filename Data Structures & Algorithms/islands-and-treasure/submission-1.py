class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if grid[r][c] == 0 :
                    queue.append((r,c,0))
        rows,cols = len(grid), len(grid[0])
        while queue :
            row,col,dis = queue.popleft()
            if row+1<rows and grid[row+1][col] == 2147483647 :
                grid[row+1][col] = dis + 1
                queue.append((row+1,col,dis+1))
            if row-1>=0 and grid[row-1][col] == 2147483647 :
                grid[row-1][col] = dis + 1
                queue.append((row-1,col,dis+1))
            if col+1<cols and grid[row][col+1] == 2147483647 :
                grid[row][col+1] = dis + 1
                queue.append((row,col+1,dis+1))
            if col-1>=0 and grid[row][col-1] == 2147483647 :
                grid[row][col-1] = dis + 1
                queue.append((row,col-1,dis+1))         
   
        