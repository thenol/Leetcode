"""
[hard]

给出一些不同颜色的盒子 boxes ，盒子的颜色由不同的正数表示。

你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k * k 个积分。

返回 你能获得的最大积分和 。

 

示例 1：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----> [1, 3, 3, 3, 1] (1*1=1 分) 
----> [1, 1] (3*3=9 分) 
----> [] (2*2=4 分)
示例 2：

输入：boxes = [1,1,1]
输出：9
示例 3：

输入：boxes = [1]
输出：1
 

提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100

https://leetcode.cn/problems/remove-boxes/description/?source=vscode
"""

# 区间dp典型题和答案整理：
"""
https://leetcode.cn/problems/remove-boxes/solutions/1884753/by-424479543-g3gt/?source=vscode
"""

from functools import cache
from itertools import groupby
class Solution:
    # method 2:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        在一起的一串一定会一起消掉，这样收益肯定最大
        1. 将在一起的一串盒子直接打包，形成新的数组
        2. 基于新的数组进行移除盒子操作

        boxes: [1,3,2,2,2,3,4,3,1]
        g: [[1, 1], [3, 1], [2, 3], [3, 1], [4, 1], [3, 1], [1, 1]]
        nums: (1, 3, 2, 3, 4, 3, 1)
        cnt:  (1, 1, 3, 1, 1, 1, 1)
        """
        g = [[a,len(list(b))] for a,b in groupby(boxes)]
        nums,cnt = zip(*g)
        @cache
        def f(i,j,c):
            """计算在区间 [i, j) 中合并箱子所需的最大得分，前面还有和nums[i]相同的c个箱子"""
            if i == j : return 0 
            c += cnt[i] 
            return max(
                [f(i+1,j,0)+c*c] + # 直接和前缀一起计算
                [f(i+1,k,0)+f(k,j,c) for k in range(i+1,j) if nums[i] == nums[k]] # 前缀也可能和其他和nums[i]相同的nums[k]一起计算；自动完成了剪枝，因为相邻且相同的盒子已经被打包在了一起
            ) 
        return f(0,len(nums),0)


    # method 1: 
    def removeBoxes(self, boxes: List[int]) -> int:
        # f(l, r, k) [l, r]上有k个后缀和r相同的情况下得分最大值
        # 
        @cache
        def f(l, r, k):
            # ✅ 左闭右开区间[l, r)：l<r，归约态判等 l==r
            # ✅ 左闭右闭区间[l, r]：l<=r，归约态判小 r<l
            if r<l: return 0 # ⭕️注意[l, r]区间范围 0<=l<=r<=len(boxes)-1：如果判断r<=r为退出条件，会少计算 l==r的情况，即区间只有一个元素的情况;

            suf = boxes[r]

            ## 遍历后缀可能和哪一部分的suf一起消掉
            # 1. 后缀先消掉
            for e in range(r, l-1, -1): 
                if boxes[e]!=suf: break
            if boxes[e] == suf: e -= 1 # ⭕️注意上述循环退出的两个条件

            ans = f(l, e, 0) + (r-e+k)**2 
            
            # 2. 后缀先不消，而是遍历所有可能，和前面的某一串boxes[r]一起消除
            for i in range(e-1, l-1, -1): # boxes[e]!=suf
                if boxes[i] == suf and boxes[i]!=boxes[i+1]: # 只考虑连续的suf中的首个，即aaa「a」baaa <-
                    # 找到新的和suf相同的串，尝试和后缀一起消掉的可能性
                    ans = max(ans, f(l, i, r-e+k) + f(i+1, e, 0))
            return ans
        
        return f(0, len(boxes)-1, 0)
