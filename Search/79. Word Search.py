'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Search algorithm
        # dynamic programming
        m=len(board)
        n=len(board[0])
        visited=[[0 for _ in range(n)]for _ in range(m)]
        def dp(s,i,j):
            nonlocal m,n,board,visited
            if not s: # boundary condition at the first place
                return True
            if not visited[i][j]==0:
                return False
            if board[i][j]==s[0]:
                visited[i][j]=1
                if not s[1:]:
                    visited[i][j]=0
                    return True
                ans= (dp(s[1:],i+1,j) if i+1<m else False) or (dp(s[1:],i-1,j) if i-1>=0 else False)\
                 or (dp(s[1:],i,j+1) if j+1<n else False) or (dp(s[1:],i,j-1) if j-1>=0 else False)
                visited[i][j]=0 # end of visiting
                return ans
        if not word:
            return True
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dp(word,i,j):
                        return True

        return False