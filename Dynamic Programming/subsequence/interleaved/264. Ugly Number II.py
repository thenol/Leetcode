'''
[medium]

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 方法1: 排序法
# version 1: heap O(NlogN)
from heapq import heappush,heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q=[]
        ugly=[2,3,5]
        heappush(q,1)
        s={1}
        while n>1:
            u=heappop(q)
            for i in ugly:
                if u*i not in s:
                    heappush(q,u*i)
                    s|={u*i}
            n-=1
        return heappop(q)

# versoin 2: triple pointer
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[1]
        i2 = i3 = i5 = 0
        c=1
        while c<n:
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)
            if ugly == nums[i2] * 2: 
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
            c+=1
        return nums[-1]



# 方法2: 动态规划法——三指针
"""
本质：三数组合并，不重不漏
https://www.cnblogs.com/yeshengCqupt/p/13629568.html

[1, 2,...]

A：{1*2，2*2，3*2，4*2，5*2，6*2，8*2，10*2......}

B：{1*3，2*3，3*3，4*3，5*3，6*3，8*3，10*3......}

C：{1*5，2*5，3*5，4*5，5*5，6*5，8*5，10*5......}
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1,]
        p2, p3, p5 = 0, 0, 0
        c = 1
        while True:
            if c == n:
                return ans[-1]
            next = min(ans[p2] * 2, ans[p3]*3, ans[p5]*5)
            if next == ans[p2] * 2:
                p2 += 1
            
            if next == ans[p3] * 3:
                p3 += 1
            
            if next == ans[p5] * 5:
                p5 += 1
            
            ans.append(next)
            c += 1