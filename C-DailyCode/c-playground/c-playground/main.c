//
//  main.c
//  c-playground
//  LeetCode - 临时代码板
//
//  Created by Crven on 20/09/27.
//

#pragma mark - 内容概述
/** 求数组中最大升序（或降序）子序列长度
 原题链接：
 https://leetcode.com/problems/longest-increasing-subsequence/?tab=Description#/description
 给定一个无序的整数数组，找到其中最长上升子序列的长度。
 举个栗子，
 示例数组 arr[] = {10, 9, 2, 5, 3, 7, 101, 18}，
 数组arr的最长的上升子序列是 {2, 3, 7, 101}，它的长度是4。
 请注意，可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
 算法的时间复杂度应该为 O(n2) 。
 进阶：能将算法的时间复杂度降低到 O(nlogn) 吗?
 */


#pragma mark - 引用头文件
#include <stdio.h>


#pragma mark - 宏定义 & 全局变量
#define DEBUG_MODE              (1)
#define DEBUG_LOG(fmt, ...)     if (DEBUG_MODE) printf(fmt, ##__VA_ARGS__)
// 测试用例
//int array[] = {10, 9, 2, 2, 3, 5, 4, 3, 5, 7, 6, 80, 7, 18, 8};
//int array[] = {10, 9, 2, 5, 3, 7, 80, 18};
int array[] = {4, 9, 4, 3, 7, 8};
int count = sizeof(array)/sizeof(int);


#pragma mark - 部分函数声明
void debugLogArrayFull(int *arr, int count);
void debugLogArrayWithoutZero(int *a, int count);


#pragma mark - O(n²)实现
/** 笔记备注
 思路：动态规划
 记录以每个index元素结尾的LIS
 */
int lengthOfLIS_on2(int* nums, int numsSize) {
    // 0个元素可直接返回结果
    if (numsSize < 1) {
        return 0;
    }
    // 维护一个动态规划数组 保存以每个index为结尾的最大上升子序列长度
    int dp[numsSize];
    DEBUG_LOG("给定数组: ");
    debugLogArrayFull(nums, numsSize);
    // 此for循环只是为了log直观 初始化dp数组中元素
    for (int i =0; i < numsSize; i++) {
        dp[i] = 0;
    }
    int i, j = 0, result = 0;
    for (i = 0; i < numsSize; i++) {
        // dp[i]初始至少是1
        dp[i] = 1;
        DEBUG_LOG("—————— i = %d ——————\n", i);
        DEBUG_LOG("外层-单步-开始 i:%2d  j:%2d  result:%2d  dp:", i, j, result);
        debugLogArrayFull(dp, numsSize);
        for (j = 0; j < i; j++) {
            DEBUG_LOG("内层-单步-开始 i:%2d  j:%2d  result:%2d  dp:", i, j, result);
            debugLogArrayFull(dp, numsSize);
            if (nums[i] > nums[j] && dp[i] < dp[j] + 1) {
                // 当前元素 大于 之前的某个元素 并且当前dp 小于 之前这个索引的dp+1 就更新当前dp
                dp[i] = dp[j] + 1;
            }
            DEBUG_LOG("内层-单步-结束 i:%2d  j:%2d  result:%2d  dp:", i, j, result);
            debugLogArrayFull(dp, numsSize);
        }
        if (result < dp[i]) {
            result = dp[i];
        }
        DEBUG_LOG("外层-单步-结束 i:%2d  j:%2d  result:%2d  dp:", i, j, result);
        debugLogArrayFull(dp, numsSize);
    }
    return result;
}

#pragma mark - O(nlogn)实现
/** 笔记备注
 思路：贪心 + 二分查找
 考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，
 因此我们希望每次在上升子序列最后加上的那个数尽可能的小。
 基于上面的贪心思路，我们维护一个数组d[i] ，表示长度为i 的最长上升子序列的末尾元素的最小值，
 用len 记录目前最长上升子序列的长度，起始时len 为1，d[1]=nums[0]。
 设当前已求出的最长上升子序列的长度为len（初始时为1），从前往后遍历数组nums，在遍历到nums[i]
 时：
 如果nums[i]>d[len] ，则直接加入到d 数组末尾，并更新len=len+1；
 否则，在d 数组中二分查找，找到第一个比nums[i] 小的数d[k] ，并更新d[k+1]=nums[i]。
 
 以输入序列[0,8,4,12,2] 为例：
 第一步插入0，d=[0]；
 第二步插入8，d=[0,8]；
 第三步插入4，d=[0,4]；
 第四步插入12，d=[0,4,12]；
 第五步插入2，d=[0,2,12]。
 最终得到最大递增子序列长度为3。
 */
// 折半(二分)查找
int binarySearch(int *array, int lenght, int key) {
    int low = 0;
    int high = lenght - 1;
    int mid;
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (array[mid] > key) {
            high = mid - 1;
        } else if (array[mid] < key) {
            low = mid + 1;
        } else {
            return mid;
        }
    }
    return low;
}

int lengthOfLIS_onlogn(int* nums, int numsSize) {
    // 长度若为0，无须比较直接返回
    if (numsSize < 1) {
        return 0;
    }
    // tmp[]为 记录长度为i的最长上升子序列的末尾元素的最小值
    int tmp[numsSize], position = 0;
    DEBUG_LOG("给定数组: ");
    debugLogArrayFull(nums, numsSize);
    // 此for循环只是为了log直观 初始化tmp数组中元素
    for (int i =0; i < numsSize; i++) {
        tmp[i] = 0;
    }
    tmp[0] = nums[0];
    int lenght = 1;
    // 从遍历nums[1]开始遍历nums数组
    for (int i = 1; i < numsSize; i++) {
        DEBUG_LOG("单步循环开始 i=%2d pos=%2d len=%2d tmp:", i, position, lenght);
        debugLogArrayWithoutZero(tmp, numsSize);
        // 若当前nums元素 > tmp最大元素，插入tmp，length++
        if (nums[i] > tmp[lenght - 1]) {
            tmp[lenght] = nums[i];
            lenght++;
            DEBUG_LOG("单步循环结束 i=%2d ------ len=%2d tmp:", i, lenght);
            debugLogArrayWithoutZero(tmp, numsSize);
        } else {
            // 二分定位 用当前nums元素 替换 tmp中合理位置元素
            position = binarySearch(tmp, lenght, nums[i]);
            tmp[position] = nums[i];
            DEBUG_LOG("单步循环结束 i=%2d pos=%2d ------ tmp:", i, position);
            debugLogArrayWithoutZero(tmp, numsSize);
        }
    }
    return lenght;
}


#pragma mark - 主函数&公共函数
int main(int argc, const char * argv[]) {
    printf("求数组中最大升序子序列长度\n");
    
    printf("\n");
    printf("O(n²)方式\n");
    int count_on2 = lengthOfLIS_on2(array, sizeof(array)/sizeof(int));
    printf("result = %d\n", count_on2);
    
    
    printf("\n");
    printf("O(nlogn)方式\n");
    int count_onlogn = lengthOfLIS_onlogn(array, sizeof(array)/sizeof(int));
    printf("result = %d\n", count_onlogn);
    
    return 0;
}

void debugLogArrayFull(int *a, int count) {
    DEBUG_LOG("{");
    for (int i = 0; i < count; i++) {
        DEBUG_LOG("%2d", a[i]);
        if (i < count - 1) {
            DEBUG_LOG(" ,");
        }
    }
    DEBUG_LOG(" }\n");
}

void debugLogArrayWithoutZero(int *a, int count) {
    DEBUG_LOG("{");
    for (int i = 0; i < count; i++) {
        if (a[i] != 0) {
            DEBUG_LOG("%2d",a[i]);
            if (i < count - 1 && a[i+1] != 0) {
                DEBUG_LOG(" ,");
            }
        }
    }
    DEBUG_LOG(" }\n");
}

#pragma mark - 整体笔记备注
/**
 整体思路
 1、子序列：不要求连续子序列，只要保证元素前后顺序一致即可；
 2、上升：这里的“上升”是“严格上升”，类似于 [2, 3, 3, 6, 7] 这样的子序列是不符合要求的。
 */
