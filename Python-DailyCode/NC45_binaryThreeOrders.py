"""
———————————————————————
Python3 
NC45_binaryThreeOrders.py
———————————————————————
个人备注
2020-10-10
似懂非懂
———————————————————————
题目出处
NC#45 实现二叉树的先序中序后序遍历
中等 栈 树 哈希
https://www.nowcoder.com/practice/a9fec6c46a684ad5a3abd4e365a9d362
———————————————————————
题目描述
分别按照二叉树先序，中序和后序打印所有的节点。
示例1:
    输入: {1,2,3}
    输出: [[1,2,3], [2,1,3], [2,3,1]]
示例2:
    输入: {1,2,3,4,5,6,7}
    输出: [[1,2,4,5,3,6,7], [4,2,5,1,6,3,7], [4,5,2,6,7,3,1]]
———————————————————————
"""

# Definition for TreeNode.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preOrder(self, root, data1, data2, data3):
        if root is None:
            return
        data1.append(root.val) # 先序：根左右
        self.preOrder(root.left, data1, data2, data3)
        data2.append(root.val) # 中序：左根右
        self.preOrder(root.right, data1, data2, data3)
        data3.append(root.val) # 后序：左右根
    
    """
    :type root: TreeNode # 二叉树根节点
    :rtype    : [[int]]  # 整型二维数组
    """
    def threeOrders(self , root):
        data1=[]
        data2=[]
        data3=[]
        self.preOrder(root, data1, data2, data3)
        result = [data1, data2, data3]
        print(result)
        return result
