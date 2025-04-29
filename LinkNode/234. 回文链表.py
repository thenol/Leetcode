"""
[easy]

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

 

示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
 

提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9
 

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

https://leetcode.cn/problems/palindrome-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：
1. 

https://leetcode.cn/problems/palindrome-linked-list/solutions/2952645/o1-kong-jian-zuo-fa-xun-zhao-zhong-jian-rv0f3/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    # 876. 链表的中间结点
    """
    由于 fast 指针的移动速度是 slow 指针的两倍，当 fast 指针遍历完整个链表时，slow 指针恰好走完链表的一半。对于奇数长度的链表，slow 指向正中间的节点；对于偶数长度的链表，slow 指向中间两个节点的后一个节点。
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # 初始化两个指针，slow和fast都指向链表的头节点
        while fast and fast.next:  # 当fast指针不为空并且fast的下一个节点也不为空时，循环继续
            slow = slow.next      # slow指针每次移动一步
            fast = fast.next.next  # fast指针每次移动两步
        return slow             # 当循环结束时，slow指针指向的就是链表的中间节点

    # 206. 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:  # 不是回文链表
                return False
            head = head.next
            head2 = head2.next
        return True
