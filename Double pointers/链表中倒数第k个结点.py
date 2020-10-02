'''
输入一个链表，输出该链表中倒数第k个结点。
要求：
    1. 一次遍历
    2. in-place
'''

# version 1: double pointer: i,j=0,k
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        count=0
        node=head
        while count<k and node:
            node=node.next
            count+=1
        if count!=k:
            return None
        pre=head
        while node:
            node=node.next
            pre=pre.next
        return pre

# 注意，如果链表打不到k个，就返回空