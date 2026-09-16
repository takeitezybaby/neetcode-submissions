class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = []          # path[row] = col of queen in that row
        cols = set()
        diag1 = set()       # row - col
        diag2 = set()       # row + col

        def backtrack(row):
            if row == n:
                result.append(path.copy())
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                path.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                path.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        # convert column-lists to board strings, if needed
        boards = []
        for path in result:
            board = []
            for col in path:
                row_str = '.' * col + 'Q' + '.' * (n - col - 1)
                board.append(row_str)
            boards.append(board)

        return boards