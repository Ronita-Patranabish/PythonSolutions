class Solution:
    def exist(self, board, word):
        n = len(board)
        m = len(board[0])
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[index]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"  # mark visited
            
            found = (
                dfs(i + 1, j, index + 1) or
                dfs(i - 1, j, index + 1) or
                dfs(i, j + 1, index + 1) or
                dfs(i, j - 1, index + 1)
            )
            
            board[i][j] = temp  # backtrack
            return found
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        
        return False