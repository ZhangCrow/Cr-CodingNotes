"""
———————————————————————
Python3 
LC70_climbingStairs.py
———————————————————————
个人备注
2020-10-11
思路没理解透彻
———————————————————————
题目出处
LC#70 爬楼梯
简单 动态规划
https://leetcode-cn.com/problems/climbing-stairs/

LC#剑指Offer.10-II 青蛙跳台阶问题
简单 递归
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/

NC#68 跳台阶
简单 递归 动态规划
https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4
———————————————————————
题目描述
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例1:
    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶
示例2:
    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶
———————————————————————
"""

class Solution:
    """
    :type n:   int
    :rtype:    int
    """
    def climbStairs(self, n):
        # if n<=2 : f(n) = n
        # if n>2 :  f(n) = f(n-1)+f(n-2)
        if n <= 2:
            return n
        # f(n-2) 初始为f(1) = 1
        # f(n-1) 初始为f(2) = 2
        # 可以这么写 pre, cur = 1, 2
        pre = 1
        cur = 2
        # 求f(n), 从3开始直至n
        for num in range(3, n+1):
            # 这三行也可以这么写 pre, cur = cur, pre + cur
            tmp = cur
            cur = cur + pre
            pre = tmp
            # 此时 f(n-1) = pre, f(n) = cur
        return cur

def main():
    case = 10
    print('case : ' + str(case))
    ret = Solution().climbStairs(case)
    print('result: ' + str(ret))

if __name__ == '__main__':
    main()

