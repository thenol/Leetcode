"""
[meidum]

定义字符串 base 为一个 "abcdefghijklmnopqrstuvwxyz" 无限环绕的字符串，所以 base 看起来是这样的：

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
给你一个字符串 s ，请你统计并返回 s 中有多少 不同非空子串 也在 base 中出现。

 

示例 1：

输入：s = "a"
输出：1
解释：字符串 s 的子字符串 "a" 在 base 中出现。
示例 2：

输入：s = "cac"
输出：2
解释：字符串 s 有两个子字符串 ("a", "c") 在 base 中出现。
示例 3：

输入：s = "zab"
输出：6
解释：字符串 s 有六个子字符串 ("z", "a", "b", "za", "ab", and "zab") 在 base 中出现。
 

提示：

1 <= s.length <= 105
s 由小写英文字母组成

https://leetcode.cn/problems/unique-substrings-in-wraparound-string/description/?source=vscode
"""

# 思路：
"""
最优解：

https://leetcode.cn/problems/unique-substrings-in-wraparound-string/solutions/432752/xi-fa-dai-ni-xue-suan-fa-yi-ci-gao-ding-qian-zhui-/?source=vscode


母题 3
我们继续扩展。

如果我让你求出不大于 k 的子数组的个数呢？不大于 k 指的是子数组的全部元素都不大于 k。 比如 [1,3,4] 子数组有 [1], [3], [4], [1,3], [3,4] , [1,3,4]，不大于 3 的子数组有 [1], [3], [1,3] ，那么 [1,3,4] 不大于 3 的子数组个数就是 3。 实现函数 atMostK(k, nums)。

参考代码（JS）:

function countSubArray(k, nums) {
  let ans = 0;
  let pre = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] <= k) {
      pre += 1;
    } else {
      pre = 0;
    }

    ans += pre;
  }
  return ans;
}

母题 4
如果我让你求出子数组最大值刚好是 k 的子数组的个数呢？ 比如 [1,3,4] 子数组有 [1], [3], [4], [1,3], [3,4] , [1,3,4]，子数组最大值刚好是 3 的子数组有 [3], [1,3] ，那么 [1,3,4] 子数组最大值刚好是 3 的子数组个数就是 2。实现函数 exactK(k, nums)。

实际上是 exactK 可以直接利用 atMostK，即 atMostK(k) - atMostK(k - 1)，原因见下方母题 5 部分。

作者：lucifer
链接：https://leetcode.cn/problems/unique-substrings-in-wraparound-string/solutions/432752/xi-fa-dai-ni-xue-suan-fa-yi-ci-gao-ding-qian-zhui-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

✅解释：
1. 为什么 最大值刚好是k 需要通过 atMostK(k) - atMostK(k - 1) 来计算，而无法直接基于循环判断 ==k 然后 pre += 1 ？
原因：注意条件 子数组❗️最大值❗️刚好是 k，如果只判断 if nums[i] == k 无法确保 pre 累加的计算的区间长度内元素都是不大于k 的，因此必须通过 atMostK(k) - atMostK(k - 1) 来计算。

""" 
# 此类模板可以解决问题包括：
#   1. 统计数组相邻差为 k 连续子数组的总个数
#   2. 统计数组不大于 k 的子数组的个数
#   3. 数组最大值刚好是 介于 k1 和 k2 的子数组的个数
#   4. 

# 相关题目：
"""
467. 环绕字符串中唯一的子字符串 (medium)
795. 区间子数组个数 (medium)
904. 水果成篮（中等）
992. K 个不同整数的子数组（困难）
"""

from collections import defaultdict
class Solution:
  # 核心思想：类似前缀和
  def findSubstringInWraproundString(self, p: str) -> int:
      p = '^' + p
      len_mapper = defaultdict(lambda: 0)
      w = 1
      for i in range(1,len(p)):
          if ord(p[i])-ord(p[i-1]) == 1 or ord(p[i])-ord(p[i-1]) == -25:
              w += 1
          else:
              w = 1
          len_mapper[p[i]] = max(len_mapper[p[i]], w) # 这就得到了去重的目的。这种算法是不重不漏的，因为最长的连续子串一定是包含了比它短的连续子串，
      return sum(len_mapper.values())