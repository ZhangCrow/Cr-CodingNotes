"""
———————————————————————
Python3 
NC105_binarySearch.py
———————————————————————
个人备注
2020-10-09
需要再次尝试
思路完全理解，代码还需熟悉
———————————————————————
题目出处
NC#105 二分查找 //变体
简单 二分
https://www.nowcoder.com/practice/7bc4a1c7c371425d9faa9d1b511fe193
———————————————————————
题目描述
请实现有重复数字的有序数组的二分查找。
输出在数组中第一个大于等于查找值的位置，如果数组中不存在这样的数，则输出数组长度加一。
示例：
    输入: 5,4,[1,2,4,4,5]
    输出: 3
———————————————————————
"""

class Solution:
    """
    :type length:   int #数组长度
    :type target:   int #查找值
    :type array:    int #一维有序数组
    :rtype:         int
    """
    def upper_bound_(self , length , target , array ):
        # 使用 low 和 high 记录数组下标
        low = 0
        high= length-1
        if array[length-1] < target:
            # 数组最大数也小于查找值 直接返回未找到
            return length+1
        while low < high:
            # 这里注意使用//来取整 二分
            mid = low+(high-low)//2
            if array[mid] >= target:
                high = mid
            else:
                low = mid+1
        # 题目要求的返回值是下标+1
        return low+1

def main():
    caseArray = [1, 2, 4, 4, 5]
    caseTarget = 4
    caseLength = 5
    print('length: ' + str(caseLength) + '  target: ' + str(caseTarget) + '  array: ' + str(caseArray))
    ret = Solution().upper_bound_(caseLength, caseTarget, caseArray)
    print('result: ' + str(ret))

if __name__ == '__main__':
    main()

