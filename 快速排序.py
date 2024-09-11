'''
 快速排序，类似打扑克拍理牌
 步骤：
 1. 选择一个基准值，通常选择第一个元素或者最后一个元素
 2. 遍历数组，将小于基准值的元素放到左边，大于基准值的元素放到右边
 3. 递归左右两边的数组，直到数组长度为1
 时间复杂度：O(nlogn)
'''

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         left = []
#         right = []
#         for i in range(1, len(arr)):
#             if arr[i] < pivot:
#                 left.append(arr[i])
#             else:
#                 right.append(arr[i])
#         return quick_sort(left) + [pivot] + quick_sort(right)


def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp: # 右边界向左移动，直到遇到小于基准值（temp）的元素
            right -= 1 # 右边界向左移动
        li[left] = li[right] # 把右边的值写到空位上
        while left < right and li[left] < temp:
            left += 1
        li[right] = li[left] # 把左边的值写到空位上
    li[left] = temp # 把基准值（temp）写到中间
    return left # 返回基准值的索引，用left和right来划分左右两边的数组


def quick_sort(li, left, right):
    if left < right: # 至少两个元素
        mid = partition(li, left, right) # 划分左右两边的数组
        quick_sort(li, left, mid - 1) # 递归左边的数组
        quick_sort(li, mid + 1, right) # 递归右边的数组
    return li


# Example
arr = [5, 3, 8, 6, 2, 7, 1, 4]
print(quick_sort(arr, 0, len(arr)-1)) # Output: [1, 2, 3, 4, 5, 6, 7, 8]