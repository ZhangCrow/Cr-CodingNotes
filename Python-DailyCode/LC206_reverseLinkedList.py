"""
———————————————————————
Python3 
LC206_reverseLinkedList.py
———————————————————————
个人备注
2020-10-09
需要再次尝试
思路完全理解，代码还需熟悉
———————————————————————
题目出处
LC#206 反转链表
简单
https://leetcode-cn.com/problems/reverse-linked-list/

LC#剑指Offer.24 反转链表
简单
https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/

NC#78 反转链表
简单 链表
https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca
———————————————————————
题目描述
反转一个单链表。
示例：
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
———————————————————————
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    双指针迭代
    :type head: ListNode
    :rtype:     ListNode
    """
    def reverseList(self, head):
        if not head or not head.next:
            return head
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

    """
    递归 - 未尝试
    """