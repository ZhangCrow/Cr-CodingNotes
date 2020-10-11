"""
———————————————————————
Python3 
LC141_linkedListCycle.py
———————————————————————
个人备注
2020-10-09
需要再次尝试
思路完全理解，代码还需熟悉
———————————————————————
题目出处
LC#141 环形链表
简单
https://leetcode-cn.com/problems/linked-list-cycle/

NC#4 判断链表中是否有环 
简单 链表 双指针
https://www.nowcoder.com/practice/650474f313294468a4ded3ce0f7898b9
———————————————————————
题目描述
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。
———————————————————————
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype:     bool
        """
        # 龟兔赛跑 有圈的话总会相遇
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

