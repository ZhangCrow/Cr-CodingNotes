//
//  main.c
//  c-playground
//  LeetCode - 临时代码板
//
//  Created by Crven on 20/09/27.
//

#pragma mark - 引用头文件
#include <stdio.h>
#include <stdbool.h>
#include <string.h>


#pragma mark - 宏定义 & 全局变量
#define swap(var1, var2)   (var1^=var2, var2^=var1, var1^=var2)

// 测试用例
int array[] = { 2, 0, 6, 1, 9, 5, 4, 7, 8, 3 };
int count = sizeof(array)/sizeof(int);


#pragma mark - 部分函数声明
void printArray(int *arr, int count);


#pragma mark - 冒泡排序
/** 笔记备注
 最基础的排序之一
 基本思路：
 每个元素和它后面的元素们依次进行大小比较是否交换位置。
 */
void bubbleSort(int *a, int count) {
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j+1]);
            }
        }
        printf("单元步骤 : i = %d  ", i);
        printArray(a, count);
    }
}

/** 笔记备注
 基本思路：
 对冒泡排序常见的改进方法是加入标志性变量flag，用于标志某一趟排序过程中是否有数据交换。
 如果进行某一趟排序时并没有进行数据交换，则说明所有数据已经有序，可立即结束排序，避免不必要的
 比较过程。
 */
void bubbleSortEx(int *a, int count) {
    bool flag = true;
    for (int i = 0; i < count - 1 && flag; i++) {
        flag = false;
        for (int j = 0; j < count - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j+1]);
                flag = true;
            }
        }
        printf("单元步骤 : i = %d  ", i);
        printArray(a, count);
    }
}

#pragma mark - 简单选择排序
/** 笔记备注
 基本思路：
 每趟从待排序的记录中选出关键字最小的记录，顺序放在已排序的记录序列末尾，直到全部排序结束为止。
 */
void selectionSort(int *a, int count) {
    int i, j, k;
    for (i = 0; i < count - 1; i++) {
        k = i;
        for (j = i + 1; j < count; j++) {
            if (a[k] > a[j]) {
                k = j;
            }
        }
        if (i != k) {
            swap(a[i], a[k]);
        }
        printf("单元步骤 : i = %d  ", i);
        printArray(a, count);
    }
}

#pragma mark - 快速排序
/** 笔记备注
 快速排序是对冒泡排序的一种改进方式，通过分治和递归的思想实现。
 基本思路：
 通过一趟排序将要排序的数据分割成独立的两部分，使分割点左边都是比它小的数，右边都是比它大的数。
 */
void quickSort(int *a, int left, int right) {
    if (left >= right) {
        return;
    }
    int i = left;
    int j = right;
    int key = a[i];
    while (i < j) {
        while (i < j && key <= a[j]) {
            j--;
        }
        a[i] = a[j];
        printf("左边部分 : i = %d, j = %d  ", i, j);
        printArray(a, count);
        while (i < j && key >= a[i]) {
            i++;
        }
        a[j] = a[i];
        printf("右边部分 : i = %d, j = %d  ", i, j);
        printArray(a, count);
    }
    a[i] = key;
    printf("单元步骤 : i = %d, j = %d  ", i, j);
    printArray(a, count);
    quickSort(a, left, i - 1);
    quickSort(a, i + 1, right);
}

#pragma mark - 主函数 & 公共函数
int main(int argc, const char * argv[]) {
    
    printf("冒泡排序\n");
    int arrA[count];
    memcpy(arrA, array, sizeof(array));
    printf("原始数组 :        ");
    printArray(arrA, count);
    bubbleSort(arrA, count);
    printf("最终结果 :        ");
    printArray(arrA, count);
    printf("\n");
    
    printf("冒泡排序优化\n");
    int arrB[count];
    memcpy(arrB, array, sizeof(array));
    printf("原始数组 :        ");
    printArray(arrB, count);
    bubbleSort(arrB, count);
    printf("最终结果 :        ");
    printArray(arrB, count);
    printf("\n");
    
    printf("简单选择排序\n");
    int arrC[count];
    memcpy(arrC, array, sizeof(array));
    printf("原始数组 :        ");
    printArray(arrC, count);
    selectionSort(arrC, count);
    printf("最终结果 :        ");
    printArray(arrC, count);
    printf("\n");
    
    printf("快速排序\n");
    int arrD[count];
    memcpy(arrD, array, sizeof(array));
    printf("原始数组 :               ");
    printArray(arrD, count);
    quickSort(arrD, 0, count - 1);
    printf("最终结果 :               ");
    printArray(arrD, count);
    printf("\n");
    
    return 0;
}

void printArray(int *arr, int count) {
    printf("{");
    for (int i = 0; i < count; i++) {
        printf("%2d", arr[i]);
        if (i < count - 1) {
            printf(",");
        }
    }
    printf(" }\n");
}

#pragma mark - 整体笔记备注
/**
 常见排序导图：
 http://upload-images.jianshu.io/upload_images/1063354-9960fd72f12384e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
 
 常见排序的复杂度：
 http://upload-images.jianshu.io/upload_images/1063354-a9187d5b43d4591a.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
 
 排序的稳定性是指如果在排序的序列中，存在前后相同的两个元素的话，排序前和排序后它们的相对位置
 不发生变化。
 */
