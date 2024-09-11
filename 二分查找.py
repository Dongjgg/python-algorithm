'''
# 二分查找算法
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
# 适用场景：有序数组查找

# 算法步骤：
# 1. 首先设置两个指针，left指向数组的第一个元素，right指向数组的最后一个元素；
# 2. 然后计算中间位置mid = (left + right) // 2；
# 3. 如果arr[mid] == target，则返回mid；
# 4. 如果arr[mid] < target，则将left指针指向mid + 1；
# 5. 如果arr[mid] > target，则将right指针指向mid - 1；
# 6. 重复步骤2-5，直到left > right，或者找到target；
# 7. 如果没有找到target，则返回-1。
'''

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # // 向下取整
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 测试
arr = [1, 3, 5, 7, 9]
target = 7
print(binary_search(arr, target)) # 3