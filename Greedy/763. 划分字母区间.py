"""
[medium]

给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。

 

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
示例 2：

输入：s = "eccbbbbdec"
输出：[10]
 

提示：

1 <= s.length <= 500
s 仅由小写英文字母组成

https://leetcode.cn/problems/partition-labels/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：
    这段代码的目标是将字符串 s 划分为尽可能多的子字符串，使得每个字母最多出现在一个子字符串中。首先，使用字典 last 记录每个字符最后出现的索引。然后，使用 start 和 end 维护当前分区的起始和结束位置。遍历字符串 s，对于每个字符，更新当前分区的结束位置 end，使其包含当前字符最后出现的位置。如果当前字符的索引等于当前分区的结束位置，说明找到了一个可以独立的分区，将分区长度加入结果列表，并更新下一个分区的起始位置。

https://leetcode.cn/problems/partition-labels/solutions/2806706/ben-zhi-shi-he-bing-qu-jian-jian-ji-xie-ygsn8/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}  # 创建一个字典，存储每个字符最后出现的索引
        ans = []  # 初始化存储结果的列表
        start = end = 0  # 初始化当前分区的起始和结束位置
        for i, c in enumerate(s):
            end = max(end, last[c])  # 更新当前分区的结束位置，确保包含当前字符最后出现的位置
            if end == i:  # 如果当前分区的结束位置等于当前字符的索引，说明找到了一个可以独立的分区
                ans.append(end - start + 1)  # 将当前分区的长度添加到结果列表中
                start = i + 1  # 更新下一个分区的起始位置
        return ans  # 返回存储分区长度的结果列表
