# -*- coding: UTF-8 -*-

# 《算法图解》第二章·选择排序 P28 选择排序

def findIndexOfMin(arr):
    min_index = 0
    min = arr[min_index]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min_index = i
            min = arr[min_index]
    return min_index

def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        min = findIndexOfMin(arr)
        new_arr.append(arr.pop(min))
        print arr
    return new_arr

print selectionSort([5, 3, 6, 2, 10])
