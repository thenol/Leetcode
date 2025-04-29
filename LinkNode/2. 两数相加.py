"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
这段代码模拟了我们手工进行加法运算的过程，从个位开始逐位相加，并处理进位。通过使用链表这种数据结构，可以表示任意长度的整数。哑节点的使用使得在处理头部时不需要进行额外的判断，使代码更加简洁。
https://leetcode.cn/problems/add-two-numbers/solutions/2327008/dong-hua-jian-ji-xie-fa-cong-di-gui-dao-oe0di/?envType=study-plan-v2&envId=top-100-liked
"""

# 好好读读题目，所有数字都是逆序存储的
# 2->4->3，也就是342
class Solution:
    # 迭代版本
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 创建一个哑节点 (dummy node)，作为结果链表的头部，方便处理进位和空链表的情况
        carry = 0  # 初始化进位为 0
        while l1 or l2 or carry:  # 当 l1, l2 中至少有一个链表还有节点，或者还有进位时，继续循环
            if l1:
                carry += l1.val  # 将 l1 当前节点的值加到进位中
                l1 = l1.next  # 将 l1 指针移动到下一个节点
            if l2:
                carry += l2.val  # 将 l2 当前节点的值加到进位中
                l2 = l2.next  # 将 l2 指针移动到下一个节点
            cur.next = ListNode(carry % 10)  # 创建一个新的节点，存储当前位数的和 (carry 除以 10 的余数)
            carry //= 10  # 计算新的进位 (carry 除以 10 的整数部分)
            cur = cur.next  # 将 cur 指针移动到新创建的节点，以便连接下一个节点
        return dummy.next  # 返回哑节点的下一个节点，即结果链表的头部

    # 递归版本
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s = carry + l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = s % 10  # 每个节点保存一个数位（直接修改原链表）
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 进位
        return l1
