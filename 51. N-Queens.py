'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        loc=lambda x: '.'*x+'Q'+'.'*(n-x-1)
        res=[]

        def dfs(visted,path,N):
            # print(path)
            if N==n:
                res.append(path)
            else:
                for i in range(n):
                    if visted[i]==-1:
                        continue
                    else:
                        check = True
                        for axis in path:
                            x,y=axis
                            k=(y-N)/(x-i)
                            if k==1 or k==-1:
                                check=False
                        if check:
                            visted[i]=-1
                            dfs(visted,path+[(i,N)],N+1)
                            visted[i]=0
        dfs([0]*n,[],0)
        result=[]
        for i in res:
            path=[]
            for j in i:
                x,y=j
                path.append(loc(x))
            result.append(path)

        return result