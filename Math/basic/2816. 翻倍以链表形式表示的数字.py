""" medium
给你一个 非空 链表的头节点 head ，表示一个不含前导零的非负数整数。

将链表 翻倍 后，返回头节点 head 。

 

示例 1：


输入：head = [1,8,9]
输出：[3,7,8]
解释：上图中给出的链表，表示数字 189 。返回的链表表示数字 189 * 2 = 378 。
示例 2：


输入：head = [9,9,9]
输出：[1,9,9,8]
解释：上图中给出的链表，表示数字 999 。返回的链表表示数字 999 * 2 = 1998 。
 

提示：

链表中节点的数目在范围 [1, 104] 内
0 <= Node.val <= 9
生成的输入满足：链表表示一个不含前导零的数字，除了数字 0 本身。

https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/description/

"""
# O(n), O(1)
# 思路：在与冷静分析，进位的条件，也就是
## 如果不考虑进位，就是每个节点的值乘以 2。
## 什么时候会受到进位的影响呢？只有下一个节点大于 4 的时候 (2*5=10，就需要进位了)，才会因为进位多加一。
## 特别地，如果链表头的值大于 4，那么需要在前面插入一个新的节点。

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        cur = head
        while cur:
            cur.val = cur.val * 2 % 10
            if cur.next and cur.next.val > 4:
                cur.val += 1
            cur = cur.next
        return head

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/solutions/2385962/o1-kong-jian-zuo-fa-kan-cheng-shi-head-y-1dco/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
