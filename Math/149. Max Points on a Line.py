'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from decimal import *
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # the goal is to traverse all lines of different gredient
        gredient={}
        N=len(points)
        if N==1:
            return 1

        init={}
        for i in points:
            if tuple(i) in init:
                init[tuple(i)]+=1
            else:
                init[tuple(i)]=1
        
        if len(init)==1:
            return init[tuple(points[0])]

        for i in range(N):
            for j in range(i+1,N):
                if tuple(points[i])==tuple(points[j]):
                    continue
                deta_x=(points[j][0]-points[i][0])
                deta_y=(points[j][1]-points[i][1])
                if deta_x==0:
                    k='inf'
                else:
                    k = Decimal(deta_y)/Decimal(deta_x)
                if k not in gredient:
                    gredient[k]={}
                    gredient[k]['index']=i
                    gredient[k]['num']=init[tuple(points[i])]+1
                else:
                    if gredient[k]['index']==i:
                        gredient[k]['num']+=1
        mx=0
        for k,v in gredient.items():
            mx = mx if mx >=v['num'] else v['num']
        return mx