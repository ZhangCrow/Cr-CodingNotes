# -*- coding: UTF-8 -*-

# 《算法图解》第四章·快速排序 P52 快速排序/合并排序
# D&C (divide and conquer) 分而治之 递归

# 快速排序
def quicksort(array):
    if len(array) < 2:
        # 基线条件：为空或只包含一个元素的数组 一定是有序的
        return array
    else :
        print "quicksort A Step Part1 " + str(array)
        # 递归条件
        pivot = array[0]
        # 由所有小于等于基准值的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]
        print "quicksort A Step Part2 " + str(less) + " + " + str(pivot) + " + " + str(greater)
        return quicksort(less) + [pivot] + quicksort(greater)


array = [5, 10, 0, 3, 2, 4, 6]
print "eg数组 " + str(array)
print "ga排序 " + str(quicksort(array))


'''
归并排序采用分而治之的原理：
一、将一个序列从中间位置分成两个序列；
二、在将这两个子序列按照第一步继续二分下去；
三、直到所有子序列的长度都为1，也就是不可以再二分截止。这时候再两两合并成一个有序序列即可。
'''

# 自己尝试的扩展 合并/归并排序
def cr_merge(array1, array2):
    array = []
    i = j = 0;
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1
    if i == len(array1):
        array += array2[j:]
    else:
        array += array1[i:]
    print "mergeSort A Step Part3 " + str(array)
    return array

def cr_mergeSort(array):
    # 分而治之 先分后治
    if len(array) <= 1:
        return array
    print "mergeSort A Step Part1 " + str(array)
    middle = len(array) / 2
    left = cr_mergeSort(array[:middle])
    right = cr_mergeSort(array[middle:])
    print "mergeSort A Step Part2 " + str(left) + " + " + str(right)
    return cr_merge(left, right)
    
    
array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print "eg数组 " + str(array)
print "cr排序 " + str(cr_mergeSort(array))
