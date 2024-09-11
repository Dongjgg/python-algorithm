'''
    顺序查找算法
'''


def seq_search(li, val):
    for index, value in enumerate(li): # enumerate 用法 遍历列表同时获得索引
        if value == val:
            return index
    return -1


if __name__ == '__main__':
    li = [1, 3, 5, 7, 9]
    val = 5
    index = seq_search(li, val)
    if index == -1:
        print(f"{val} not found in the list")
    else:
        print(f"{val} found at index {index}")