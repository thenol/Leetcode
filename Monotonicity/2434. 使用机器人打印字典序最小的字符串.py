"""
中等

给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：

删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
请你返回纸上能写出的字典序最小的字符串。

 

示例 1：

输入：s = "zza"
输出："azz"
解释：用 p 表示写出来的字符串。
一开始，p="" ，s="zza" ，t="" 。
执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
示例 2：

输入：s = "bac"
输出："abc"
解释：用 p 表示写出来的字符串。
执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。
执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。
执行第一个操作，得到 p="ab" ，s="" ，t="c" 。
执行第二个操作，得到 p="abc" ，s="" ，t="" 。
示例 3：

输入：s = "bdda"
输出："addb"
解释：用 p 表示写出来的字符串。
一开始，p="" ，s="bdda" ，t="" 。
执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。
执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。
 

提示：

1 <= s.length <= 105
s 只包含小写英文字母。

https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/
"""

# 注意字符串操作看这个帖子 https://blog.csdn.net/weixin_44322764/article/details/106845144
# string.ascii_lowercase 存放着所有ascii码的小写字母

from string import ascii_lowercase
from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        ans = []
        cnt = Counter(s)
        min = 0
        st = []
        for c in s:
            cnt[c] -= 1
            while min < 25 and cnt[ascii_lowercase[min]] == 0: # 通过这个有序的ascii_lowercase来控制顺序
                min += 1
            st.append(c) # 这个操作比较简练，不管字符是什么，先入站，然后在下一步再去判断是否该出栈
            while st and st[-1] <= ascii_lowercase[min]:
                ans.append(st.pop())
        
        return "".join(ans)

