'''
选择排序(Selection Sort)是一种简单直观的排序算法。
它的工作原理是从待排序的数据元素中选出最小(最大)的一个元素，
存放在序列的起始位置，然后，再从剩余未排序元素中继续寻找最小(最大)的元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

步骤：
1. 首先在未排序序列中找到最小(最大)元素，存放到排序序列的起始位置。
2. 再从剩余未排序元素中继续寻找最小(最大)元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。
'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 寻找最小(最大)元素的索引
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 交换最小(最大)元素与第一个元素
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 测试
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr)) # [11, 12, 22, 25, 64]