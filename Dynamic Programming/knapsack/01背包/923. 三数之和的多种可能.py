"""
[medium]

给定一个整数数组 arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且 arr[i] + arr[j] + arr[k] == target 的元组 i, j, k 的数量。

由于结果会非常大，请返回 109 + 7 的模。

 

示例 1：

输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举(arr[i], arr[j], arr[k])：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
示例 2：

输入：arr = [1,1,2,2,2,2], target = 5
输出：12
解释：
arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
 

提示：

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300

https://leetcode.cn/problems/3sum-with-multiplicity/description/?source=vscode
"""

from functools import cache
class Solution:
    # method 2: 01背包——迭代式
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # state: d[i][j][k] 表示在arr[:i]的范围内，选取j个数，形成k的可能性
        # 0<=i<=N;0<=j<=3;0<=k<=target
        N = len(arr) # i
        M = 10**9+7
        Q = 3 # j
        d = [[0]*(target+1) for j in range(Q+1)] # 身略i

        # initialization
        # 1<=i; 1<=j; 0<=k<=target
        d[0][0] = 1

        # transition
        for i in range(1, N+1):
            for j in range(Q, 0, -1): # 注意j的取值范围为 1<=j<=Q，也就是1，可以取到啊，[左闭右开)；如果取不到，那
                for k in range(target, -1, -1):
                    if 0<=k-arr[i-1]:
                        d[j][k] = (d[j][k] + d[j-1][k-arr[i-1]]) % M
        """
        初始化和计算顺序的思考：
        1. 三步走初始化战略仍然是不变的：d[0][0] = 1
        
        问题1: 其次思考，在上述初始化后，其他的究竟还需不需要进行初始化？
            本质上来讲，
                1. d[0][0]意味着所有状态的出发点；
                2. 或者所有状态的归约点；
            其他任何状态d[j][k]，只有到达d[0][0]才意味着，找到了一个正确的解；而对于任何其他的边界情况，例如d[j][k]，例如d[0][2]都是无解的情况，而无解的情况，默认都是0。因此，只需要初始化这一个等式就够了。

            综上所述，d[0][0] = 1，意味着：
                1. 当j==0时且k==0时，d[0][0]为1，
                2. 同时仅当d[i][j]转移到了d[0][0]状态，才意味着找到了正确的解
            
            也就是意味着从d[0][0]状态出发转移到的最终d[Q][target]状态才是合法的，或者正确解的通路，累加的可能性个数才是正确的。
            
            其他默认状态都是0

            ❗️注意：从此处也可以发散出去，可能归约点有多个情况，那么显而易见，也需要 多个归约点 或者 集合 进行初始化。具体参见 序列——字符串 上的初始化。
        
        问题2: 之前的初始化策略还是否可行？
            显然，可行，上述的方式d[0][0] = 1，很明显是最简单的方式，而如果按照之前的初始化方式：
            # k==0
            for j in range(Q+1):
                d[j][0] = 1 if j==0 else 0 # ❌：这里其实是有问题的，即使k为0，如果arr中有0，且1<j，那么同样是可以选择的；即使，真这么赋值，虽然是错的，但是仍然最终结果是对的，因为，最后会被 d[0][0] = 1 这个正确初始化后，计算结果覆盖，也就是被正确的结果覆盖了
            
            # j==0
            for k in range(target+1):
                d[0][k] = 1 if k==0 else 0
            d[0][0] = 1
        """
        
        return d[Q][target] # j, k


    # method 1: 01背包问题
    # MLE：注意问题规模，三位数组，3000*100*300=10^7，因此会爆内存限制
    # 继续修改成迭代式，并且对内存进行优化
    def threeSumMulti_1(self, arr: List[int], target: int) -> int:
        # state: d[i][j][k] 表示在arr[:i]的范围内，选取j个数，形成k的可能性
        # 0<=i<=N;0<=j<=3;0<=k<=target
        N = len(arr)
        M = 10**9+7
        Q = 3
        self.arr = arr
        self.target = target

        @cache
        def f(i, j, k):
            """表示在arr[:i]的范围内，选取j个数，形成k的可能性"""
            nonlocal M, arr
            # print(i, j, k)
            # initialization
            # 如何有意义的初始化
            # ❌：乱猜初始化，总是会漏掉情况
            # if j==0 and k==0: return 1 # d[0][0][0] = 1
            # if i==0 or j==0 or k==0: return 0
            
            # ✅：有序讨论初始化
            # 关注，i,j，只需要讨论i, j的正常访问，不越界即可
            # 空数组
            if i==0:
                if j==0 and k==0: return 1
                else: return 0
            # 空次数
            if j==0 and k!=0: return 0

            # transition
            ans = f(i-1, j, k) # 不放i-1

            # 放得下i-1
            if 0<=k-arr[i-1]:
                ans += f(i-1, j-1, k-arr[i-1])
            return ans % M
        return f(N, Q, target)
  