"""
[hard]
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = [["0"]]
输出：0
示例 3：

输入：matrix = [["1"]]
输出：1
 

提示：

rows == matrix.length
cols == matrix[0].length
1 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'

https://leetcode.cn/problems/maximal-rectangle/description/?source=vscode
"""

# 思路：预处理 + 单调栈
# 单调站： 哨兵 + 边界处理

# version 1.1:
from math import inf
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        arr = [[0]*C for _ in range(R)]
        for j in range(C): # 初始化首行
            arr[0][j] = int(matrix[0][j])
        for i in range(1, R):
            for j in range(C):
                if matrix[i][j] == '0':
                    arr[i][j] = 0
                else:
                    arr[i][j] = arr[i-1][j]+1
        
        def get_s(lst):
            """求lst最大面积"""

            # 恭请左右护法，且最终左右护法都不会出栈，因此也不会影响结果，舍己为人
            stk = [(-1, -inf)] # 左哨兵，控制左边界，且不影响 lst 下标
            lst.append(-1) # 右哨兵，控制右边界，确保所有 lst 中元素都能够顺利出栈；

            ans = [0]*len(lst)

            for i in range(len(lst)):
                while stk and lst[i] <= stk[-1][1]:
                    t = stk.pop()
                    ans[t[0]] = (i-stk[-1][0]-1)*t[1] # 减去两边比t小的树，注意这个距离应该是 i-stk[-1][0]-1, 解释 stk[-1][0]... t[0] ... i，而stk[-1][1]和lst[i]都是比t[1]最近的小的元素
                stk.append((i, lst[i]))
            return max(ans)
        return max(get_s(arr_item) for arr_item in arr)

# version 1: 标准哨兵写法
from math import inf
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # preprocess
        bar_arr = [[int(item) for item in matrix[0]]]
        r, c = len(matrix), len(matrix[0])
        for i in range(1, r):
            tmp = [0] * c
            for j in range(c):
                if matrix[i][j] == "1":
                    tmp[j] = 1 + bar_arr[-1][j]
                else:
                    tmp[j] = 0
            
            bar_arr.append(tmp)
        
        # 单调栈
        def f(arr):
            stk = [[-inf, -1]] # 左护法
            arr.append(0) # 右护法
            l = [-1] * len(arr)
            r = [-1] * len(arr)
            for i in range(len(arr)):
                while stk and stk[-1][0] >= arr[i]: # 相同元素，前一个元素会由后面一个元素剔除出栈
                    r[stk.pop()[1]] = i # 找到右边界
                if stk:
                    l[i] = stk[-1][1] # 找到i的左边界
                stk.append([arr[i], i]) # 进栈
            
            # print(l ,r)
            mx = 0
            for i in range(len(arr)-1):
                # 注意细节 r[i] - l[i] - 1
                # 当连续两个元素相等时，两个元素的累加面积会由后面一个元素得出
                mx = max(mx, (r[i] - l[i] -1)*arr[i]) 
            return mx
        
        mx = 0
        for a in bar_arr:
            mx = max(mx, f(a))
        return mx

# version 2: 业余哨兵写法
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # preprocess
        bar_arr = [[int(item) for item in matrix[0]]]
        r, c = len(matrix), len(matrix[0])
        for i in range(1, r):
            tmp = [0] * c
            for j in range(c):
                if matrix[i][j] == "1":
                    tmp[j] = 1 + bar_arr[-1][j]
                else:
                    tmp[j] = 0
            
            bar_arr.append(tmp)
        
        # 单调栈
        def f(arr):
            extend_arr = [float('-inf')] + arr + [float('-inf')]
            stk = []
            l = [-1] * len(extend_arr)
            r = [-1] * len(extend_arr)
            for i in range(len(extend_arr)):
                while stk and extend_arr[stk[-1]] >= extend_arr[i]: # 相同元素，前一个元素会由后面一个元素剔除出栈
                    r[stk.pop()] = i # 找到右边界
                if stk:
                    l[i] = stk[-1] # 找到i的左边界
                stk.append(i) # 进栈
            
            # print(l ,r)
            mx = 0
            for i in range(1, len(extend_arr)-1):
                # 注意细节 r[i] - l[i] - 1
                # 当连续两个元素相等时，两个元素的累加面积会由后面一个元素得出
                mx = max(mx, (r[i] - l[i] -1)*extend_arr[i]) 
            return mx
        
        mx = 0
        for a in bar_arr:
            mx = max(mx, f(a))
        return mx
