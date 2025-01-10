"""
[medium]

给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

 

示例 1：

输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1
0 <= k <= nums.length

https://leetcode.cn/problems/max-consecutive-ones-iii/description/?source=vscode
"""
from itertools import accumulate
import bisect
class Solution:
    # 思路出发点：连续区间+前缀和+二分查找
    # method 6: 不等式 => 二分查找；O(nlogn)
    # 用常规的数据结构，简单不容易错
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        方法一：二分查找
        思路与算法

        P[right]−P[left]≤k

        即P[right]−P[left]的上界为k，当P[left]越小，整体值越大
        等价于

        P[left]≥P[right]−k       (1)
        也就是说，我们需要找到最小的满足 (1) 式的 left。由于数组 A 中仅包含 0/1，因此前缀和数组是一个单调递增的数组，我们就可以使用二分查找的方法得到 left。

        解释：不等式 => 二分查找
        1. 因为越小的left，意味着可以填充更多的0，也就能实现更大的连续1序列和
        2. 为什么能转换成二分查找相关：✅本质需要构造一个递增序列，然后用于二分查找，而前缀和就是一个递增序列
            P[right]−k ≤ P[left]
            首先 P[right]−k 是严格递增序列；
            其次，在这样的严格递增序列中，寻找 P[right]−k ≤ P[left]=P[x]
            即搜索数组为 P，搜索目标为 已知值 P[right]−k，搜索到的下标为 left或者x 
            因此 bisect_left(P, P[right]−k)
        
        结构解释：
        查找到的结果P[left]，满足条件[left, right) 【❗️左闭右开❗️】，在这样的区间内，0的个数 P[right]−P[left]≤k，而且P[left]尽可能的小，也就是区间[left, right)为能翻转的最大的区间，因此，此时形成的最大连续1序列长度为 right-left

        """
        N = len(nums)
        pre_s = list(accumulate([1-item for item in nums], initial=0))

        ans = 0
        for right in range(1, N+1):
            left = bisect.bisect_left(pre_s, pre_s[right]-k) # 对应的[:right]区间
            ans = max(ans, right-left)
        
        return ans


    # method 5: 滑动窗口 O(n)
    # 用常规的数据结构，简单不容易错
    def longestOnes_5(self, nums: List[int], k: int) -> int:
        # state: d[i] 表示以i结尾的填充最多k个值的连续 1 的最大个数
        N = len(nums)
        q = []
        zero = 0
        d = [0] * N
        for i in range(N):
            zero += 0 if nums[i] else 1
            q.append(nums[i])
            while k<zero and q: # 滑动窗口，维护固定的2个0的窗口; 而且遍历了所有以i结尾可能的窗口，覆盖了所有的可能性
                zero -= 0 if q.pop(0) else 1

            d[i] = len(q)
        
        return max(d)

    # method 4: O(N)
    # 很复杂，不好写，还容易错
    # WA：代码逻辑太复杂——涉及4个变量的操作以及复杂判断，总体代码不鲁棒
    def longestOnes_1(self, nums: List[int], k: int) -> int:
        # state: d[i] 表示以i结尾的填充最多k个值的连续 1 的最大个数
        N = len(nums)
        d = [0]*N
        i, j = N-1, N-1
        zero = 0
        if i==0: return k
        while 0<i and 0<j:
            # while 0<j and zero <= k: ❌：循环退出的时候，zero=k+1
            while 0<=j and zero <= k:
                if nums[j] == 0:
                    zero += 1
                j -= 1
            # d[i] = N-1-j # ❌：明显错误，和i相关
            if 0<=j or zero == k+1: # 查找成功，zero=k+1，j指向zero前1个元素
                d[i] = i-j-1
            else:  # 查找失败: 0<=zero<=k；e.g., 11100111
                d[i] = i-j
            zero = zero if nums[i] else (zero-1)
            print(i, j, zero)
            i -= 1
        print(d)
        return max(d)
        

    # method 3: 01背包——空间优化
    # 本质：先计算表格第一行，然后后续从第二行开始，可以基于第一行的数据开始推理填充后续表格;
    # ⭕️：改写空间优化时，非优化版本的一个步骤都不能缺少
    # TLE：看数据规模，显然会超时，O(N^2)
    def longestOnes_3(self, nums: List[int], k: int) -> int:
        # state: d[i][j] 表示以i结尾，翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数
        # 0<=i<N;0<=j<=k
        N = len(nums)
        d = [1]*(k+1) # i==0的时候；接下来计算i in range(1, N)

        # initialization
        d[0] = nums[0] # i==0的时候，初始没有翻转次数，则主要由nums[0]决定

        # transition
        ans = 0
        for i in range(1, N):
            # print(d)
            """
            for j in range(k, 0, -1):
                d[j] = (d[j] + 1) if nums[i] else (d[j-1] + 1)
            """
            # print(d)
            for j in range(k, -1, -1):
                if j == 0: # ⭕️：遗漏这一列表格填写；当j==0的时候，需要单独处理，类似于初始化；如果不填写，就会一致是初始化值
                    d[j] = (d[j] + 1) if nums[i] else 0
                else:
                    d[j] = (d[j] + 1) if nums[i] else (d[j-1] + 1)
                
                # ⭕️：注意最优解是max([d[i][k] for i in range(N)])
                # 内存优化之后，自然同样是表格中第k列下的最大值，即 max({d[0][k], d[1][k],...})
                if j == k:
                    ans = max(ans, d[k])
        return ans

    # method 2: 任意0子序列+可变条件变量k => 01背包
    # 状态表示：元素状态
    # MLE;O(N^2)
    def longestOnes_2(self, nums: List[int], k: int) -> int:
        # state: d[i][j] 表示以i结尾，翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数
        # 0<=i<N;0<=j<=k
        N = len(nums)
        d = [[0]*(k+1) for _ in range(N)]

        # initialization
        # i==0
        for j in range(1, k+1):
            d[0][j] = 1 # 高于1次可翻转，一定为1
        # j==0
        d[0][0] = nums[0] # 没有翻转次数，则主要由nums[0]决定
        for i in range(1, N):
            # d[i][0] = d[i-1][0]+1 if nums[i] else d[i-1][0] # 错误1❌：初始化错误
            d[i][0] = d[i-1][0]+1 if nums[i] else 0

        # transition
        """
        for i in range(1, N):
            for j in range(1, k+1):
                d[i][j] = d[i-1][j] # 不翻转；错误2❌：不翻转的时候想当然，转移写错，明显需要分两种情况讨论
                if nums[i] == 0: # 翻转一次
                    d[i][j] = max(d[i][j], d[i-1][j-1]+1) # 此关系存在
                elif nums[i]: # nums[i]==1，不用翻转
                    d[i][j] = d[i-1][j] + 1
        """
        for i in range(1, N):
            for j in range(1, k+1):
                if nums[i] == 0: # 翻转，可以得到以i结尾的最大序列
                    d[i][j] = d[i-1][j-1] + 1
                else: # 不需要翻转
                    d[i][j] = d[i-1][j] + 1
        # print(d)
        return max([d[i][k] for i in range(N)])

    # method 1: 任意0子序列+可变条件变量k => 01背包
    # 状态表示：范围状态
    # ❌：不能只知道套模板，状态转移方程，一定要满足其充要条件，必须能够正确地用来表示题设关系；而本题中，题目里面的关系无法用模板中的转移方程来描述，或者该转移方程不成立
    def longestOnes_1(self, nums: List[int], k: int) -> int:
        # state: d[i][j] 表示nums[:i]范围最多 k 个 0 ，则返回 数组中连续 1 的最大个数
        # 0<=i<=N;0<=j<=k
        N = len(nums)
        d = [[0]*(k+1) for _ in range(N+1)]

        # initialization
        

        # transition
        for i in range(1, N+1):
            for j in range(k+1):
                d[i][j] = d[i-1][j] # 不翻转
                if nums[i-1] == 0: # 可以翻转
                    # 复杂度较高，每次都需要遍历计算最长的连续1的个数
                    # ❌：此0不一定能和前d[i-1][j-1]连起来，因此以下转移方程的关系是错的，或者不存在以下的转移方程关系
                    # d[i][j] = max(d[i][j], d[i-1][j-1]+1)
                    ...
