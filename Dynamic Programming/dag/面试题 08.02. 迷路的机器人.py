'''
[medium]

设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。



网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释: 
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/robot-in-a-grid-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# version 1: TLE

class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        # 自下而上
        r,c=len(obstacleGrid),len(obstacleGrid[0])
        ans=[]
        def walk(i,j,path):
            nonlocal ans
            if ans: return 
            # if obstacleGrid[i][j]==-1:return
            if i==r-1 and j==c-1:
                ans=path
            else:
                if i+1<r and obstacleGrid[i+1][j]==0:
                    walk(i+1,j,path+[[i+1,j]])
                if j+1<c and obstacleGrid[i][j+1]==0:
                    walk(i,j+1,path+[[i,j+1]])
                if not ans:
                    # obstacleGrid[i][j]=-1
        if obstacleGrid[0][0]!=0:return []
        walk(0,0,[[0,0]])
        return ans


# VERSION 2: AC
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        # 自下而上
        r,c=len(obstacleGrid),len(obstacleGrid[0])
        ans=[]
        def walk(i,j,path):
            nonlocal ans
            if ans: return 
            if obstacleGrid[i][j]==-1:return # 剪枝，即使[i,j]==0, 如果路径不存在，也剪掉
            if i==r-1 and j==c-1:
                ans=path
            else:
                if i+1<r and obstacleGrid[i+1][j]==0:
                    walk(i+1,j,path+[[i+1,j]])
                if j+1<c and obstacleGrid[i][j+1]==0:
                    walk(i,j+1,path+[[i,j+1]])
                if not ans:
                    obstacleGrid[i][j]=-1 # 状态的记录
        if obstacleGrid[0][0]!=0:return []
        walk(0,0,[[0,0]])
        return ans

        
        