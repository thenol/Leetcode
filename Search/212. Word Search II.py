'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# version 1： time limit exceeded
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dic={}
        M=len(board)
        N=len(board[0])
        
        # initialization
        for i in range(M):
            for j in range(N):
                if board[i][j] in dic:
                    dic[board[i][j]].append((i,j))
                else:
                    dic[board[i][j]]=[(i,j)]
        vis=[[0 for _ in range(N)]for _ in range(M)]
        
        # dfs 
        def dfs(i,j,s):
            nonlocal vis
            # ------------------------- boundary check
            if not s:
                return True
            if i==-1 or i==M or j==-1 or j==N or vis[i][j]:
                return False
            # -------------------------

            else:
                ans=False
                if s[0]==board[i][j]:
                    vis[i][j]=1
                    ans = dfs(i-1,j,s[1:]) or dfs(i+1,j,s[1:])\
                    or dfs(i,j-1,s[1:]) or dfs(i,j+1,s[1:])
                    vis[i][j]=0 # end of visiting
                return ans
        
        # main
        res=set()
        for w in words:
            if w[0] in dic:
                for v in dic[w[0]]:
                    i,j=v
                    if dfs(i,j,w):
                        res.add(w)
        return list(res)

                    


                    
