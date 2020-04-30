'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        m=len(board)
        n=len(board[0])
        visited=[[-1 if board[i][j]=='X' else 0 for j in range(n)]for i in range(m)]
        def BFS(i,j):
            visited[i][j]=1
            queue=[(i,j)]
            path=[(i,j)]
            closed=True
            while queue:
                x,y=queue.pop(0)
                if x==0 or x==m-1 or y==0 or y==n-1: # In fact, this is a problem with graphics. Note that special judgment does not affect the traversal of the graph.
                    closed=False
                if x-1>=0 and visited[x-1][y]==0:
                    path.append((x-1,y))
                    queue.append((x-1,y))
                    visited[x-1][y]=1
                if y-1>=0 and visited[x][y-1]==0:
                    path.append((x,y-1))
                    queue.append((x,y-1))
                    visited[x][y-1]=1
                if x+1<m and visited[x+1][y]==0:
                    path.append((x+1,y))
                    queue.append((x+1,y))
                    visited[x+1][y]=1
                if y+1<n and visited[x][y+1]==0:
                    path.append((x,y+1))
                    queue.append((x,y+1))
                    visited[x][y+1]=1
            return path if closed else closed
        def flip(arr):
            for x,y in arr:
                board[x][y]='X'
        for i in range(m):
            for j in range(n):                    
                if board[i][j]=='O' and visited[i][j]==0:
                    path=BFS(i,j)
                    if path:
                        flip(path)
    
