# -*- coding: UTF-8 -*-

# 《算法图解》第四章·快速排序 P47 分而治之-练习
# D&C (divide and conquer) 分而治之 递归

# 个人练习 数组求元素总和
def cr_sum(arr):
    if len(arr) == 0:
        return 0
    else :
        return arr.pop(0) + sum(arr)

# 标准答案
def ga_sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

# 标准答案 计算列表的元素数量
def ga_count(list):
    if list == []:
        return 0
    return 1 + ga_count(list[1:])
    
# 个人练习 找出列表中的最大的数字
def cr_findMax(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        return arr[1]
    else:
        sub_max = cr_findMax(arr[1:])
        if arr[0] > sub_max:
            return arr[0]
        return sub_max

# 标准答案 找出列表中的最大的数字
def ga_findMax(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = ga_findMax(list[1:])
        return list[0] if list[0] > sub_max else sub_max
        
# 标准答案 找出列表中的最大的数字 个人改进
def ga2_findMax(list):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    elif len(list) == 2:
        sub_max = list[1]
    else:
        sub_max = ga2_findMax(list[1:])
    return list[0] if list[0] > sub_max else sub_max


arr = [0, 2, 3, 4, 6]
#arr = []
print "eg数组 " + str(arr)
#print "cr求和 " + str(cr_sum(arr)) # 不该有pop(0)操作
print "ga求和 " + str(ga_sum(arr))
print "ga数量 " + str(ga_count(arr))
print "cr最大 " + str(cr_findMax(arr))
print "ga最大 " + str(ga_findMax(arr))
print "ga2最大 " + str(ga2_findMax(arr))
