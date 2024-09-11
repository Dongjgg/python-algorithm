'''
    冒泡排序(Bubble Sort)是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
步骤：
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # range(n)不包括n，所以最后一次循环只比较n-1次
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # 等价于java里面的 int temp = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = temp;  写法
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 改进
def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):  # range(n)不包括n，所以最后一次循环只比较n-1次
        exchange = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # 等价于java里面的 int temp = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = temp;  写法
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                exchange = True
        if not exchange:  # 如果没有发生交换，说明已经排序好了，可以提前结束循环
            break
    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr), len(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
