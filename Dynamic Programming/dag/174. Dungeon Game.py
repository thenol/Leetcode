'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dungeon-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # dynamic programming
        # state: d[i][j] means the minimum value needed to reach to princess(s.t. d[i][j]>=1 !!!!important)
        M=len(dungeon)
        N=len(dungeon[0])
        d=[[0 for _ in range(N)] for _ in range(M)] 
        d[M-1][N-1]=max(1,0-dungeon[M-1][N-1]+1)
        # initialization
        for i in range(M-2,-1,-1):
            d[i][N-1]=max(d[i+1][N-1]-dungeon[i][N-1],1)
        for j in range(N-2,-1,-1):
            d[M-1][j]=max(d[M-1][j+1]-dungeon[M-1][j],1)
        # calculation
        for i in range(M-2,-1,-1):
            for j in range(N-2,-1,-1):
                d[i][j]=max(min(d[i+1][j]-dungeon[i][j],d[i][j+1]-dungeon[i][j]),1)
        # print(d)
        return d[0][0]


# First, find the state via the last step
    # d[i][j] means the minimum value needed to reach the princess, s.t. d[i][j]>=1
# second, transition formulas
    # the way to fill in the table
# initialization:
    # boundary situation
# calculation
    # loop to fill in table



