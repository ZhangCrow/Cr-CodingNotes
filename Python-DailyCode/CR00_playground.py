# -*- coding: UTF-8 -*-

'''
——————————————————————————
 LC00_playground
 LeetCode笔记 - 临时代码板
——————————————————————————
'''


class Solution:
    def sortColors(self, nums):
    # def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1

    def upper_bound_(self , length , target , arr ):
        index = length
        left = 0
        right = length - 1
        if arr[length - 1] < target:
            return length + 1
        while(left < right):
            mid = left + (right - left) / 2
            if (arr[mid] >= target):
                if (mid < target):
                    index = mid
                    right = mid - 1
            else:
                left = mid + 1
        return index + 1

arr = [2,0,2,1,1,0]
arr = [1,2,4,4,5]
obj = Solution()
# obj.sortColors(arr)
result = obj.upper_bound_(5, 4, arr)
print(result)

