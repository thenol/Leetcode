"""
[medium]

给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。

我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

返回数组能分成的最多块数量。

 

示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
对每个块单独排序后，结果为 [0, 1], [2], [3], [4]
 

提示:

n == arr.length
1 <= n <= 10
0 <= arr[i] < n
arr 中每个元素都 不同

https://leetcode.cn/problems/max-chunks-to-make-sorted/description/?source=vscode
"""

# 本质竟然是一个非连续子序列问题，确实经典

class Solution:
    # 解决问题的关键，是能够实现，拆分之后和原来排序后的数组相同
    # 充要条件：对arr中每个元素它对应的下标就在自己的块中
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # state: d[i]表示arr[:i]范围能拆分成的最多快数量
        # 0<=i<=N
        N = len(arr)
        d = [0]*(N+1)

        # initialization
        ...
        def check(arr, j, i):
            for k in range(j, i):
                if j<=arr[k]<i: continue
                else: return False
            return True

        # transition
        for i in range(N+1):
            for j in range(i):
                # 反向推理，寻找可行的拆分点，缩减规模
                block_left = min(arr[j:i]) #
                if 0<=block_left<i and check(arr, j, i):
                    d[i] = max(d[i], d[block_left] + 1)
        
        # print(d)
        return d[N]
