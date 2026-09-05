class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if grid[r][c] == 1 :
                    fresh += 1
                if grid[r][c] == 2 :
                    queue.append((r,c,0))
        count = 0
        time = 0 
        rows,cols = len(grid), len(grid[0])
        while queue :
            row,col,ctime = queue.popleft()
            time = ctime
            if row+1<rows and grid[row+1][col] == 1 :
                grid[row+1][col] = 2
                count+=1
                queue.append((row+1,col,ctime+1))
            if row-1>=0 and grid[row-1][col] == 1 :
                grid[row-1][col] = 2
                count+=1
                queue.append((row-1,col,ctime+1))
            if col+1<cols and grid[row][col+1] == 1 :
                grid[row][col+1] = 2
                count+=1
                queue.append((row,col+1,ctime+1))
            if col-1>=0 and grid[row][col-1] ==1 :
                grid[row][col-1] = 2
                count+=1
                queue.append((row,col-1,ctime+1))
        if count == fresh :
            return time
        else :
            return -1

