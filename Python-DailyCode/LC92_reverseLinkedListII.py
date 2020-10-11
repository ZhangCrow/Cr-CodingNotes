"""
———————————————————————
Python3 
LC92_reverseLinkedListII.py
———————————————————————
个人备注
2020-10-10
循环里range(n-m)关键步骤没搞懂
———————————————————————
题目出处
LC#92 反转链表 II
中等 链表
https://leetcode-cn.com/problems/reverse-linked-list-ii/

NC#21 链表内指定区间反转
中等 链表
https://www.nowcoder.com/practice/b58434e200a648c589ca2063f1faf58c
———————————————————————
题目描述
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明: 1 ≤ m ≤ n ≤ 链表长度。
示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL
———————————————————————
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    :type head: ListNode
    :type m   : int
    :type n   : int
    :rtype    : ListNode
    """
    def reverseBetween(self, head, m, n):
        if not head or not head.next or m >= n:
            return head
        nhead = ListNode(0)
        nhead.next = head
        cur = head
        pre = nhead

        # # 别人的解法
        # for i in range(m-1):
        #     pre = cur
        #     cur = cur.next
        # for i in range(n-m):
        #     tmp = cur.next
        #     cur.next = tmp.next
        #     tmp.next = pre.next
        #     pre.next = tmp
        # return nhead.next

        index = 1
        while index < n:
            if index < m:
                pre = cur
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            index += 1
        return nhead.next
