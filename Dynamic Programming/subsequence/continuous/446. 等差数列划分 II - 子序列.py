"""
[hard]

给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。

如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

 

示例 1：

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
示例 2：

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。
 

提示：

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1

https://leetcode.cn/problems/arithmetic-slices-ii-subsequence/description/?source=vscode
"""

# 核心思路：仍然在于总结出前一项和后一项之间的转移关系，然后缩减规模
# 核心点：
#   仍然在于分析最后一步：本题中为最后一个元素加入，带来的新的弱等差序列的个数
#   假设 最后一个元素是 nums[i]，则对于其前面的元素 nums[j]，(nums[j], nums[i])之间的差为 d，则对于以nums[j]结尾的所有的等差序列加上 nums[i]都会形成新的等差序列，个数为 d[j][d]，多增加的是1个弱等差序列，因此f[i][d]+=f[j][d]+1
"""
我们首先考虑至少有两个元素的等差子序列，下文将其称作弱等差子序列。

由于尾项和公差可以确定一个等差数列，因此我们定义状态 f[i][d] 表示尾项为 nums[i]，公差为 d 的弱等差子序列的个数。

我们用一个二重循环去遍历 nums 中的所有元素对 (nums[i],nums[j])，其中 j<i。将 nums[i] 和 nums[j] 分别当作等差数列的尾项和倒数第二项，则该等差数列的公差 d=nums[i]−nums[j]。由于公差相同，我们可以将 nums[i] 加到以 nums[j] 为尾项，公差为 d 的弱等差子序列的末尾，这对应着状态转移 f[i][d]+=f[j][d]。同时，(nums[i],nums[j]) 这一对元素也可以当作一个弱等差子序列，故有状态转移

 f[i][d]+=f[j][d]+1

由于题目要统计的等差子序列至少有三个元素，我们回顾上述二重循环，其中「将 nums[i] 加到以 nums[j] 为尾项，公差为 d 的弱等差子序列的末尾」这一操作，实际上就构成了一个至少有三个元素的等差子序列，因此我们将循环中的 f[j][d] 累加，即为答案。

代码实现时，由于 nums[i] 的范围很大，所以计算出的公差的范围也很大，我们可以将状态转移数组 f 的第二维用哈希表代替。
"""