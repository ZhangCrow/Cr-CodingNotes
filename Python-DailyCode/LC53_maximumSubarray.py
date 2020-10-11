"""
———————————————————————
Python3 
LC53_maximumSubarray.py
———————————————————————
个人备注
2020-10-10
思路没理解透彻
———————————————————————
题目出处
LC#53 最大子序和
简单
https://leetcode-cn.com/problems/maximum-subarray/

LC#剑指Offer.42 连续子数组的最大和
简单
https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/


NC#19 子数组的最大累加和问题
简单 分治 动态规划
https://www.nowcoder.com/practice/554aa508dd5d4fefbf0f86e5fe953abd
———————————————————————
题目描述
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)，空间复杂度为O(1)
示例：
    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
———————————————————————
"""

class Solution:
    """
    :type nums:   List[int]
    :rtype:       int
    """
    def maxSubArray(self, nums):
        if len(nums) < 1:
            return float('nan')
        max = nums[0]
        dp_prev = 0 #记录dp[i-1]
        dp_cur = nums[0] #记录dp[i]
        for val in nums:
            dp_cur = val
            if dp_prev > 0:
                dp_cur += dp_prev
            if dp_cur >= max:
                max = dp_cur
            dp_prev = dp_cur
        return max

    """
    作者：jyd
    链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/mian-shi-ti-42-lian-xu-zi-shu-zu-de-zui-da-he-do-2/
    :type nums:   List[int]
    :rtype:       int
    """
    def maxSubArray2(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

def main():
    case = [-2,1,-3,4,-1,2,1,-5,4]
    print('array : ' + str(case))
    ret = Solution().maxSubArray(case)
    print('result: ' + str(ret))

if __name__ == '__main__':
    main()

