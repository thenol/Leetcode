'''
[medium]

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/game-of-life
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    board=[]
    st={
            1:1,
            0:0,
            3:1, # live to dead
            2:0, # dead to live
        }
    st_verse={
        1:1,
        0:0,
        3:0, # live to dead
        2:1, # dead to live
    }
    M=0
    N=0
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board=board
        M=len(board)
        N=len(board[0])
        self.M=M
        self.N=N
        for i in range(M):
            for j in range(N):
                board[i][j]=self.state(i,j)
        
        for i in range(M):
            for j in range(N):
                board[i][j]=self.st_verse[board[i][j]]
   
    def val(self,i,j):
        if i<0 or j<0 or i>=self.M or j>=self.N:
            return 0
        else:
            return self.st[self.board[i][j]]

    def count(self,i,j):
        s=0
        s+=self.val(i-1,j)+self.val(i+1,j)+self.val(i,j-1)+self.val(i,j+1)+self.val(i-1,j-1)+\
        self.val(i+1,j+1)+self.val(i-1,j+1)+self.val(i+1,j-1)
        return s

    def state(self,i,j):
        n=self.count(i,j)
        if self.board[i][j]==1:
            if n<2:
                return 3 # live to dead
            if n==2 or n==3:
                return 1 # live to live
            if n>3:
                return 3 # live to dead
        else:
            if n==3:
                return 2 # dead to live
        return self.board[i][j]