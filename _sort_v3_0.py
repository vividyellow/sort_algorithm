#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Revision : _sort_v3_0.py
# @Author : vivid_yellow
# @Date : 2020-5-6 09:54:45

# Previous version : _sort_v2_0.py
# Function :
"""
    实现10大排序算法，先自己敲一遍，再看答案修正一遍
    _01_bubble_sort_v1, _01_bubble_sort_v2, _02_selection_sort_v1, _03_insertion_sort_v1,
    _04_shell_sort_v1, _05_merge_sort_v1, _06_quick_sort_v1, _06_quick_sort_v2, _07_heap_sort_v1, _07_heap_sort_v2, _07_heap_sort_v3,
    _08_counting_sort_v1, _09_bucket_sort_v1, _10_radix_sort_v1, _10_radix_sort_v2

    _01_bubble_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _01_bubble_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _02_selection_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _03_insertion_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _04_shell_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _05_merge_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _06_quick_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _06_quick_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _07_heap_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _07_heap_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _07_heap_sort_v3(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1], ascending=True):
    _08_counting_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    _09_bucket_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1], bucket_count=5):
    _10_radix_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):  # 数字位数：3/4/5【自动计算！根据第一遍遍历得到的max_value、highest_bit】
    _10_radix_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):  # 数字位数：3/4/5【自动计算！根据第一遍遍历得到的max_value】
"""
# Description of Changes :
"""
    方便统计步骤总数，增加一个全局变量COUNT。这样针对排序算法里面调用其他排序算法的情况，也很方便统计总的步骤数。
    _03_insertion_sort_v函数的“break  # 这一段必须提前！否则i==j的情况下（即碰到那里当即确定位置为最后）没有break，然后还会继续再往前比较，还是>=的！”
    arr[k] = sorted_list.pop(0)  # 可以pop出指定的任意index位置的元素！
    
    # 找到首、中、尾[0, len_arr // 2, len_arr - 1]三个位置的值的中值作为pivot
    # 【方法2（自己实现的求取3个数的中值的算法）】
    
    list_heap[current], list_heap[parent] = list_heap[parent], list_heap[current]
                current = parent
                parent = (current - 1) // 2  # 这里搞错了，用current - 1 代替i - 1（不再是i）
    
    current = max_index  # 这个地方一定要用max_index!!!不能用left啊！【min_index那里也一样】
                    left = 2 * current + 1
                    right = 2 * current + 2
new:
    函数重新命名，梳理下注释。_07_heap_sort_v3是综合两种排序：顺序、逆序（引入一个ascending输入参数控制调用哪个）
    radix_sort的子函数名由x_sort改名为radix_sort
    dict_result[arr[0]] += 1
    _10_radix_sort_v1单独增加一次循环找出max_value，得到highest_bit
    所有函数增加了注释，调整了注释
"""
# Remarks :
"""

"""

# from PIL import Image
# import time
import numpy as np
from functools import wraps
import collections
import random

COUNT = 0


def dec_print_func_name(func):
    """装饰器：打印当前函数名"""

    @wraps(func)  # 使用本条命令可以让func函数返回其本身的函数名等。
    def inner(*args, **kwargs):
        print("\n现在执行{}函数: ".format(func.__name__))
        return func(*args, **kwargs)

    return inner


@dec_print_func_name
def _01_bubble_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """bubble_sort冒泡排序：相邻两个比对，最大的冒泡到排序好区的左端
    待改进：到上次交换处即可
    """

    len_arr = len(arr)
    global COUNT
    original_count = COUNT
    for i in range(len_arr - 1):
        for j in range(len_arr - 1 - i):
            COUNT += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Total count: {}".format(COUNT - original_count))
    print("arr: {}".format(arr))
    return arr


@dec_print_func_name
def _01_bubble_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """bubble_sort冒泡排序：相邻两个比对，最大的冒泡到排序好区的左端
    改进的冒泡算法：到上次交换处（使用一个max_index）即可【但是如果第一次的时候就是排序好的，最后一次交换的位置初始值是哪个？一直不会变】
    """

    len_arr = len(arr)
    global COUNT
    original_count = COUNT
    max_index = len_arr
    for i in range(len_arr - 1):
        is_swaped = False
        for j in range(len_arr - 1 - i):
            COUNT += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                max_index = j
                is_swaped = True

            if j > max_index:  # 到上次最大交换位置处即止（后续的项不用看了，从后往前推理：“每一个”都超过以前的）
                break
        if is_swaped == False:  # 第一次就是排序好的情况，以及已经排序好了（一趟下来，没有发生一次交换）
            break

    print("Total count: {}".format(COUNT - original_count))
    print("arr: {}".format(arr))
    return arr


@dec_print_func_name
def _02_selection_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """选择排序：一遍找出一个最大的放到排序好区的左端"""

    len_arr = len(arr)
    global COUNT
    original_count = COUNT
    for i in range(len_arr - 1):
        max_index = 0
        for j in range(1, len_arr - i):
            # print("arr: {}; count: {}".format(arr, count))
            COUNT += 1
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != len_arr - 1 - i:
            arr[max_index], arr[len_arr - 1 - i] = arr[len_arr - 1 - i], arr[max_index]

    print("Total count: {}".format(COUNT - original_count))
    print("arr: {}".format(arr))
    return arr


@dec_print_func_name
def _03_insertion_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """插入排序：左边排序好，右边的第一个插入到左边适当位置（如果原始列表基本排序ok，则很快就能排序好"""

    len_arr = len(arr)
    global COUNT
    original_count = COUNT

    for i in range(len_arr - 1):
        # 每次对第i+1个元素处理，插入前面队列（已经排序好）中【一直往前比较，直到比前一个元素大就排后面，或者一直比到第一个时候，还是没比它大，就插到它前面】
        for j in range(i, -1, -1):
            print("arr: {}; count: {}".format(arr, COUNT))
            COUNT += 1
            if arr[i + 1] >= arr[j]:
                if i != j:  # 与最后一个比对就比它大，留在原位不操作！（此处是其他情况，做操作），但是两种情况下都要break（所以break必须提前确保两种情况都执行，否则……）
                    tmp = arr.pop(i + 1)
                    arr.insert(j + 1, tmp)
                break  # 这一段必须提前！否则i==j的情况下（即碰到那里当即确定位置为最后）没有break，然后还会继续再往前比较，还是>=的！
            elif j == 0:
                tmp = arr.pop(i + 1)
                arr.insert(0, tmp)
                break

    print("Total count: {}".format(COUNT - original_count))
    print("arr: {}".format(arr))
    return arr


@dec_print_func_name
def _04_shell_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """shell排序：对03_insertion_sort的改进：不断调整步长（从一半总长（基本上两个一小队），到1/4（4个一小队），……直到间隔为1（所有的一小队）），
    然后同一步长取样到的组成小队列内部用“插入排序”排好序
    """

    len_arr = len(arr)
    global COUNT
    original_count = COUNT

    step = len_arr // 2
    while step >= 1:

        for i in range(step):  # 根据逐步缩小至1的步长，分成若干组，组内再采用插入法排序
            tmp_index_list = []
            k = i
            while k <= len_arr - 1:  # 每个组从头间隔step跑到尾得到一个组的所有成员的index
                tmp_index_list.append(k)
                k += step

            # 获取组内元素列表
            # tmp_list = list(np.array(arr)[tmp_index_list])
            tmp_list = [arr[stem] for stem in tmp_index_list]
            print("tmp_list: {}".format(tmp_list))

            # 对小组值排序
            sorted_list = _03_insertion_sort_v1(tmp_list)
            print("sorted_list: {}".format(sorted_list))

            # 再按顺序插回原来的位置
            if step != 1:
                k = i
                while k <= len_arr - 1:  # 每个组从头间隔step跑到尾得到一个组的所有成员的index
                    arr[k] = sorted_list.pop(0)  # 不采用pop方法的话，index递增
                    k += step
            else:
                arr = sorted_list[:]
                # return arr

            print("每一步后得到的arr: {}".format(arr))

        step = step // 2

    # for i in range(len_arr - 1):
    #     # 每次对第i+1个元素处理，插入前面队列（已经排序好）中【一直往前比较，直到比前一个元素大就排后面，或者一直比到第一个时候，还是没比它大，就插到它前面】
    #     for j in range(i, -1, -1):
    #         print("arr: {}; COUNT: {}".format(arr, COUNT))
    #         COUNT += 1
    #         if arr[i + 1] >= arr[j]:
    #             if i != j:
    #                 tmp = arr.pop(i + 1)
    #                 arr.insert(j + 1, tmp)
    #                 break
    #         elif j == 0:
    #             tmp = arr.pop(i + 1)
    #             arr.insert(0, tmp)
    #             break

    print("Total count: {}".format(COUNT - original_count))
    print("arr: {}".format(arr))
    return arr


def merge_two_sorted_list(sorted_arr1, sorted_arr2):
    """把排序好的两块的结果合并到一起就得到大排序的最终结果"""

    global COUNT
    merged_arr = []
    while (sorted_arr1 and sorted_arr2):
        COUNT += 1
        if sorted_arr1[0] == sorted_arr2[0]:
            merged_arr.append(sorted_arr1.pop(0))
            merged_arr.append(sorted_arr2.pop(0))
        elif sorted_arr1[0] < sorted_arr2[0]:
            merged_arr.append(sorted_arr1.pop(0))
        else:
            merged_arr.append(sorted_arr2.pop(0))

    merged_arr.extend(sorted_arr1)
    merged_arr.extend(sorted_arr2)

    return merged_arr


def split_long_list(arr0):
    """长的原始数组被拆分为两块（除非已经是1个元素）（就不拆分了）"""

    len_arr0 = len(arr0)

    if len_arr0 > 1:
        block_size = len_arr0 // 2

        arr1 = arr0[0:block_size]
        arr2 = arr0[block_size:]

    # elif len_arr0 == 1:
    #     arr1 = arr0
    #     arr2 = []
    # elif len_arr0 == 0:
    #     arr1, arr2 = [], []

    return arr1, arr2


def merge_sort(arr):
    """大排序分为三个步骤：1，长的原始数组被拆分为两块（除非已经是1个元素）（就不拆分了）；2，两块分别递归执行“大排序”，得到排序好的各自的结果；3，把排序好的两块的结果合并到一起就得到大排序的最终结果"""

    # 长的原始数组被拆分为两块（除非已经是1个元素）（就不拆分了）
    if len(arr) <= 1:
        print("数组已经不可再分了：{}".format(arr))
        return arr

    arr1, arr2 = split_long_list(arr)

    # 两块分别递归执行“大排序”，得到排序好的各自的结果【必须有递归终止的条件】
    sorted_arr1 = merge_sort(arr1)
    sorted_arr2 = merge_sort(arr2)

    # 把排序好的两块的结果合并到一起就得到大排序的最终结果
    merged_arr = merge_two_sorted_list(sorted_arr1, sorted_arr2)

    print("merged_arr: {}".format(merged_arr))
    return merged_arr


@dec_print_func_name
def _05_merge_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """归并排序：先两两元素排序好，然后四四排序好，……总之，每次两个拍好序的队列一一比对，合并为一个大的排好序的队列，直到整个队列：
    大排序分为三个步骤：1，长的原始数组被拆分为两块（除非已经是1个元素）（就不拆分了）；2，两块分别递归执行“大排序”，得到排序好的各自的结果；
    3，把排序好的两块的结果合并到一起就得到大排序的最终结果
    """

    global COUNT
    original_count = COUNT

    merged_arr = merge_sort(arr)

    print("Total count: {}".format(COUNT - original_count))
    print("最终的arr: {}".format(merged_arr))
    return merged_arr


def quick_sort_v1(arr):
    """基本快速排序方法（采用第0个作为pivot）"""

    global COUNT

    if len(arr) < 2:
        return arr
    pivot = arr[0]
    low = 1
    high = len(arr) - 1

    while (low <= high):
        while (low <= high and arr[low] < pivot):
            low += 1
            COUNT += 1

        while (low <= high and arr[high] >= pivot):
            high -= 1
            COUNT += 1

        if low < high:
            COUNT += 1
            arr[low], arr[high] = arr[high], arr[low]
    arr[0], arr[high] = arr[high], arr[0]
    print("arr: {}".format(arr))

    left = arr[:high]
    center = arr[high]
    right = arr[high + 1:]

    sorted_left = quick_sort_v1(left)
    sorted_right = quick_sort_v1(right)

    return sorted_left + [center] + sorted_right


def quick_sort_v2(arr):
    """改进的快速排序方法：取[0, len_arr // 2, len_arr - 1]三者的中值（2种方法，一种是直接调用其他排序算法：list_tmp.sort(key=lambda x:x[1])，另外一种是自己写的底层算法）作为pivot"""

    global COUNT

    len_arr = len(arr)

    if len(arr) < 2:
        return arr

    # # 找到首、中、尾[0, len_arr // 2, len_arr - 1]三个位置的值的中值作为pivot
    # # 【方法1（调用了其他排序算法，不够意思，不够底层）】
    # list_tmp = []
    # for i in [0, len_arr//2, len_arr-1]:
    #     list_tmp.append((i,arr[i]))
    # list_tmp.sort(key=lambda x:x[1])
    #
    # pivot_index = list_tmp[1][0]
    # if pivot_index != 0:
    #     arr[pivot_index], arr[0] = arr[0], arr[pivot_index]
    # pivot = list_tmp[1][1]

    # 找到首、中、尾[0, len_arr // 2, len_arr - 1]三个位置的值的中值作为pivot
    # 【方法2（自己实现的求取3个数的中值的算法）】
    # index_min = 0
    # index_max = 0
    list_tmp = []
    list_index_in_orginal_list = [0, len_arr // 2, len_arr - 1]
    for i in list_index_in_orginal_list:
        list_tmp.append(arr[i])

    (index_min_in3, index_max_in3) = (0, 1) if list_tmp[0] <= list_tmp[1] else (1, 0)
    index_center_in3 = index_min_in3 if list_tmp[2] <= list_tmp[index_min_in3] else (
        index_max_in3 if list_tmp[2] > list_tmp[index_max_in3] else 2)

    pivot_index = list_index_in_orginal_list[index_center_in3]
    pivot = arr[pivot_index]
    if pivot_index != 0:
        arr[pivot_index], arr[0] = arr[0], arr[pivot_index]

    low = 1
    high = len(arr) - 1

    while (low <= high):
        while (low <= high and arr[low] < pivot):
            low += 1
            COUNT += 1

        while (low <= high and arr[high] >= pivot):
            high -= 1
            COUNT += 1

        if low < high:
            COUNT += 1
            arr[low], arr[high] = arr[high], arr[low]
    arr[0], arr[high] = arr[high], arr[0]
    print("arr: {}".format(arr))

    left = arr[:high]
    center = arr[high]
    right = arr[high + 1:]

    sorted_left = quick_sort_v2(left)
    sorted_right = quick_sort_v2(right)

    return sorted_left + [center] + sorted_right


@dec_print_func_name
def _06_quick_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """快速排序1（基本快速排序方法（采用第0个作为pivot））：随机在队列中取一个元素，小于它的移到左边，大于等于它的移到右边。然后左边、右边分别继续各自随机取一个元素，……，如此继续直到只有1个元素？
    实际上是low往右滑动，找到高于pivot(支点; 枢轴; 中心点; 最重要的人(或事物); 中心; 核心)，high从末尾往左滑动，找到第一个小于pivot的点，二者交换位置，如此，直到low和high越过（low先行！）
    然后high位置的值跟pivot交换！

    # 随机（必须随机吗？）【直接取第1个，也可以取（第一个、中间一个、最后一个三者的中值）】取一个数作为基准，小于它的放左边【左边的那些再继续这个操作】，大于它的放右边【右边的那些再继续这个操作】。
    如此递归，直到分块只有1个元素为止
    """

    global COUNT
    original_count = COUNT

    sorted_arr = quick_sort_v1(arr)

    print("Total count: {}".format(COUNT - original_count))
    print("最终的arr: {}".format(sorted_arr))
    return arr


@dec_print_func_name
def _06_quick_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """快速排序2（改进的快速排序方法：取[0, len_arr // 2, len_arr - 1]三者的中值作为pivot）：
    随机在队列中取一个元素，小于它的移到左边，大于等于它的移到右边。然后左边、右边分别继续各自随机取一个元素，……，如此继续直到只有1个元素？
    实际上是low往右滑动，找到高于pivot(支点; 枢轴; 中心点; 最重要的人(或事物); 中心; 核心)，high从末尾往左滑动，找到第一个小于pivot的点，二者交换位置，如此，直到low和high越过（low先行！）
    然后high位置的值跟pivot交换！

    # 随机（必须随机吗？）【直接取第1个，也可以取（第一个、中间一个、最后一个三者的中值）】取一个数作为基准，小于它的放左边【左边的那些再继续这个操作】，大于它的放右边【右边的那些再继续这个操作】。
    如此递归，直到分块只有1个元素为止
    """

    global COUNT
    original_count = COUNT

    sorted_arr = quick_sort_v2(arr)

    print("Total count: {}".format(COUNT - original_count))
    print("最终的arr: {}".format(sorted_arr))
    return arr


@dec_print_func_name
def _07_heap_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """堆排序1【从大到小的顺序】：先建堆，再不断的取堆最大元素（最小元素则建相应的堆）"""

    # print("原始arr:{}".format(arr))
    len_arr = len(arr)
    global COUNT
    original_count = COUNT

    # 先建堆：从第一个开始，小的左边，大的右边
    list_heap = []
    for i in range(len_arr):
        list_heap.append(arr[i])
        current = i
        parent = (i - 1) // 2
        while (parent >= 0):
            COUNT += 1
            if list_heap[current] < list_heap[parent]:
                list_heap[current], list_heap[parent] = list_heap[parent], list_heap[current]
                current = parent
                parent = (current - 1) // 2  # 这里搞错了，用current - 1 代替i - 1（不再是i）
                # print("current:{}".format(current))
                # print("parent:{}".format(parent))
            else:
                break
        print("实时的list_heap:{}".format(list_heap))

    print("建堆后的arr:{}".format(list_heap))

    # 再取数、构建新堆（循环直到全部取出）
    sorted_list = []
    while (list_heap):
        sorted_list.append(list_heap.pop(0))
        # end_item = list_heap.pop(-1)
        # list_heap.insert(0,end_item)
        if len(list_heap) <= 1:
            continue
        list_heap.insert(0, list_heap.pop(-1))
        print("实时的list_heap:{}".format(list_heap))

        current = 0
        left = 2 * current + 1
        right = 2 * current + 2

        while (left < len(list_heap)):
            COUNT += 1
            if right < len(list_heap):  # 右子树存在的情况，需要跟他们两个比较，如果都比她们小，就跟它们中最大的交换
                (min_value, min_index) = (list_heap[left], left) if list_heap[left] < list_heap[right] else (
                    list_heap[right], right)
                if list_heap[current] > min_value:
                    list_heap[current], list_heap[min_index] = list_heap[min_index], list_heap[current]
                    current = min_index  # 这里必须是min_index，不能写left或者right啊！
                    left = 2 * current + 1
                    right = 2 * current + 2
                else:
                    break
            else:
                if list_heap[current] > list_heap[left]:
                    list_heap[current], list_heap[left] = list_heap[left], list_heap[current]
                    current = left
                    left = 2 * current + 1
                    right = 2 * current + 2
                else:
                    break

    print("Total count: {}".format(COUNT - original_count))
    print("sorted_list:{}".format(sorted_list))
    return sorted_list


@dec_print_func_name
def _07_heap_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """堆排序【从小到大的顺序】：先建堆，再不断的取堆最大元素（最小元素则建相应的堆）"""

    # print("原始arr:{}".format(arr))
    len_arr = len(arr)
    global COUNT
    original_count = COUNT

    # 先建堆：从第一个开始，小的左边，大的右边
    list_heap = []
    for i in range(len_arr):
        list_heap.append(arr[i])
        current = i
        parent = (i - 1) // 2
        while (parent >= 0):
            COUNT += 1
            if list_heap[current] > list_heap[parent]:
                list_heap[current], list_heap[parent] = list_heap[parent], list_heap[current]
                current = parent
                parent = (current - 1) // 2  # 这里搞错了，用current - 1 代替i - 1（不再是i）
                # print("current:{}".format(current))
                # print("parent:{}".format(parent))
            else:
                break
        print("实时的list_heap:{}".format(list_heap))

    print("建堆后的arr:{}".format(list_heap))

    # 再取数、构建新堆（循环直到全部取出）
    sorted_list = []
    while (list_heap):
        sorted_list.append(list_heap.pop(0))
        # end_item = list_heap.pop(-1)
        # list_heap.insert(0,end_item)
        if len(list_heap) <= 1:
            continue
        list_heap.insert(0, list_heap.pop(-1))
        print("实时的list_heap:{}".format(list_heap))

        current = 0
        left = 2 * current + 1
        right = 2 * current + 2

        while (left < len(list_heap)):
            COUNT += 1
            if right < len(list_heap):  # 右子树存在的情况，需要跟他们两个比较，如果都比她们小，就跟它们中最大的交换【如果一样大呢？】
                (max_value, max_index) = (list_heap[left], left) if list_heap[left] > list_heap[right] else (
                    list_heap[right], right)
                if list_heap[current] < max_value:
                    list_heap[current], list_heap[max_index] = list_heap[max_index], list_heap[current]
                    current = max_index  # 这个地方一定要用max_index!!!不能用left啊！
                    left = 2 * current + 1
                    right = 2 * current + 2
                else:
                    break
            else:
                if list_heap[current] < list_heap[left]:
                    list_heap[current], list_heap[left] = list_heap[left], list_heap[current]
                    current = left
                    left = 2 * current + 1
                    right = 2 * current + 2
                else:
                    break

    print("Total count: {}".format(COUNT - original_count))
    print("sorted_list:{}".format(sorted_list))
    return sorted_list


@dec_print_func_name
def _07_heap_sort_v3(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1], ascending=True):
    """堆排序【可选：顺序、逆序】：先建堆，再不断的取堆最大元素（最小元素则建相应的堆）"""

    if ascending:
        return _07_heap_sort_v2(arr)
    else:
        return _07_heap_sort_v1(arr)


@dec_print_func_name
def _08_counting_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):
    """计数排序：最大-最小，然后做成一个个的字典key，来计数。最后再一个个按顺序取出来得到排序后的序列
    【BinSort：会直接将数34放在数组的下标34处（BinSort想法非常简单，首先创建数组A[MaxValue]；然后将每个数放到相应的位置上（例如17放在下标17的数组位置）；最后遍历数组，即为排序后的结果。）】
    """
    len_arr = len(arr)
    if len_arr < 2:
        return arr
    global COUNT
    original_count = COUNT

    min_value = arr[0]
    max_value = arr[0]
    dict_result = collections.defaultdict(lambda: 0)  # 也可以直接用int代替“lambda: 0”
    dict_result[arr[0]] += 1
    for i in range(1, len_arr):
        COUNT += 1
        if arr[i] > max_value:
            max_value = arr[i]
        elif arr[i] < min_value:
            min_value = arr[i]

        dict_result[arr[i]] += 1

    sorted_list = []
    for i in range(min_value, max_value + 1):
        COUNT += 1
        sorted_list.extend([i] * dict_result[i])

    print("Total count: {}".format(COUNT - original_count))
    print("sorted_list: {}".format(sorted_list))
    return sorted_list


@dec_print_func_name
def _09_bucket_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1], bucket_count=5):
    """桶排序（假设数列是均匀分布）：【大桶（有顺序）【比如100以内的数，可以先放进10个桶：0~10；11~20；……】，直接扔在桶里，里面还有小桶】（属于一种排序思想，小桶里面可以调用其他任意的排序方法）"""

    len_arr = len(arr)
    global COUNT
    original_count = COUNT

    max_value = max(arr)  # 增加一次循环，找出最大值

    # 定义若干桶（计数排序其实是每个数确保有一个桶（min ~ max间的数都有一个桶）的桶排序）
    # 这里就定义10个桶吧（平均分为10个区间）【但是又保证每个桶至少间隔1个（min_step)以上的数字，至多20个(max_step)】
    min_step = 1
    max_step = 20
    norm_step = max_value // bucket_count
    step_size = min(max(norm_step, min_step), max_step)
    print("step_size: {}".format(step_size))

    bucket_count = np.ceil(max_value / step_size)
    print("真实的bucket_count: {}".format(bucket_count))

    # 遍历一遍，所有数放入相应的桶中
    dict_result = collections.defaultdict(list)
    for item in arr:
        COUNT += 1
        bucket_no_belong = item // step_size
        dict_result[bucket_no_belong].append(item)

    sorted_list = []
    for i in range(int(bucket_count)):
        COUNT += 1
        # 每个桶内的数据使用其他排序方法排序

        sorted_list_i = _07_heap_sort_v1(dict_result[i])

        # 将各个桶里排序好的数据拼接起来就行了
        sorted_list.extend(sorted_list_i)

    print("Total count: {}".format(COUNT - original_count))
    print("sorted_list: {}".format(sorted_list))
    return sorted_list


def get_current_bit(number, higher_bit):
    """给定一个数，得到其指定位上的值：higher_bit为0时，得到个位的数字；为1时，得到十位的；为2时，得到百位的"""

    below_bits = number % (10 ** (higher_bit + 1))
    current_bit = below_bits // (10 ** (higher_bit))

    return current_bit


def radix_sort(arr, higher_bit):
    """从高位开始，放入一个个大桶中，再大桶中的数列根据低一位来放入各个中桶。再小桶，直到最后一位按照最小桶"""

    global COUNT
    original_count = COUNT

    if higher_bit < 0:
        return arr

    len_arr = len(arr)

    dict_units_bit = collections.defaultdict(list)  # 也可以直接用int代替“lambda: 0”

    sorted_list = []
    for i in range(len_arr):
        COUNT += 1
        current_bit = get_current_bit(arr[i], higher_bit)
        dict_units_bit[current_bit].append(arr[i])

    for j in range(10):
        COUNT += 1
        sorted_list_tmp = radix_sort(dict_units_bit[j], higher_bit - 1)
        sorted_list.extend(sorted_list_tmp)

    return sorted_list


@dec_print_func_name
def _10_radix_sort_v1(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):  # 数字位数：3/4/5【自动计算！根据第一遍遍历得到的max_value、highest_bit】
    """基数排序1：最高位优先(Most Significant Digit first)法，简称MSD法【需要用到递归！】【还需要】

    基数排序：根据桶排序而来【比如：扑克牌排序法（多个顺序）】
    基数排序（radix sort）属于“分配式排序”（distribution sort），
    又称“桶子法”（bucket sort）或bin sort，顾名思义，它是透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用，
    基数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。
    有两种：一种先大桶，再小桶；另一种先小类排序（排序好后），再依次根据大类排序。如果还有更大类分类，再根据更大类排序
    最高位优先(Most Significant Digit first)法，简称MSD法【需要用到递归！】：先按k1排序分组，同一组中记录，关键码k1相等，再对各组按k2排序分成子组，
    之后，对后面的关键码继续这样的排序分组，直到按最次位关键码kd对各子组排序后。再将各组连接起来，便得到一个有序序列。
    最低位优先(Least Significant Digit first)法，简称LSD法【简单，不需要用到递归！】：先从kd开始排序，再对kd-1进行排序，依次重复，直到对k1排序后便得到一个有序序列。
    """

    # len_arr = len(arr)
    global COUNT
    original_count = COUNT

    max_value = max(arr)
    highest_bit = len(str(int(max_value))) - 1  # 还有没有更好的方法？ print(math.floor(math.log10(9.9)))
    sorted_list = radix_sort(arr, highest_bit)

    print("Total count: {}".format(COUNT - original_count))
    print("sorted_list: {}".format(sorted_list))
    return sorted_list


@dec_print_func_name
def _10_radix_sort_v2(arr=[2, 1, 0, 3, 6, 6, 4, 5, 5, 8, 1]):  # 数字位数：3/4/5【自动计算！根据第一遍遍历得到的max_value】
    """基数排序2：最低位优先(Least Significant Digit first)法，简称LSD法：先从kd开始排序，再对kd-1进行排序，依次重复，直到对k1排序后便得到一个有序序列。【简单，不需要用到递归！】

    基数排序：根据桶排序而来【比如：扑克牌排序法（多个顺序）】
    基数排序（radix sort）属于“分配式排序”（distribution sort），
    又称“桶子法”（bucket sort）或bin sort，顾名思义，它是透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用，
    基数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。
    有两种：一种先大桶，再小桶；另一种先小类排序（排序好后），再依次根据大类排序。如果还有更大类分类，再根据更大类排序
    最高位优先(Most Significant Digit first)法，简称MSD法：先按k1排序分组，同一组中记录，关键码k1相等，再对各组按k2排序分成子组，
    之后，对后面的关键码继续这样的排序分组，直到按最次位关键码kd对各子组排序后。再将各组连接起来，便得到一个有序序列。
    最低位优先(Least Significant Digit first)法，简称LSD法：先从kd开始排序，再对kd-1进行排序，依次重复，直到对k1排序后便得到一个有序序列。
    """

    len_arr = len(arr)
    global COUNT
    original_count = COUNT

    dict_units_bit = collections.defaultdict(list)  # 也可以直接用int代替“lambda: 0”
    i = 0
    highest_bit = 0  # 第一遍遍历时得到最大值
    while i <= highest_bit:
        # 从低位一直到最高位（这个最高位怎么得来，遍历一次才行啊？遍历一次后做调整？）
        sorted_list = []
        if i == 0:
            max_value = arr[0]  # 得到最大值，求得highest_bit
            for j in range(len_arr):
                # 遍历每一个列表
                COUNT += 1

                if arr[j] > max_value:
                    max_value = arr[j]

                # below_bits = arr[j] % (10 ** (i + 1))  # 这里一开始不小心写成了*，结果出现%20这种【而且还要括号括起来！！否则当写成*的时候，先对10求余再乘以（i+1）了】
                # print("below_bits【{}】 = arr[j]【{}】 % 10**(i+1)【{}】".format(below_bits, arr[j], 10 ** (i + 1)))
                # current_bit = below_bits // (10 ** (i))
                # print(" current_bit【{}】 = below_bits【{}】 // 10**(i)【{}】 ".format(current_bit, below_bits, 10**i))
                current_bit = get_current_bit(arr[j], i)
                dict_units_bit[current_bit].append(arr[j])

            highest_bit = len(str(int(max_value))) - 1  # 还有没有更好的方法？ print(math.floor(math.log10(9.9)))
            print("highest_bit: {}".format(highest_bit))
        else:
            for j in range(len_arr):
                # 遍历每一个列表
                COUNT += 1

                # below_bits = arr[j] % (10 ** (i + 1))  # 这里一开始不小心写成了*，结果出现%20这种【而且还要括号括起来！！否则当写成*的时候，先对10求余再乘以（i+1）了】
                # print("below_bits【{}】 = arr[j]【{}】 % 10**(i+1)【{}】".format(below_bits, arr[j], 10 ** (i + 1)))
                # current_bit = below_bits // (10 ** (i))
                # print(" current_bit【{}】 = below_bits【{}】 // 10**(i)【{}】 ".format(current_bit, below_bits, 10 ** (i)))
                current_bit = get_current_bit(arr[j], i)
                dict_units_bit[current_bit].append(arr[j])

        for k in range(10):
            COUNT += 1
            sorted_list.extend(dict_units_bit[k])
            # print("dict_units_bit[{}]: {}".format(k, dict_units_bit[k]))
        arr = sorted_list[:]
        dict_units_bit.clear()
        i += 1
        print("中间的arr结果: {}".format(arr))
        print("dict_units_bit: {}".format(dict_units_bit))

    print("Total count: {}".format(COUNT - original_count))
    print("最终的arr: {}".format(arr))
    return arr


def main():
    """
    """

    # arr = range(0, 1, 1)
    # arr = range(10, 0, -1)
    # arr = list(arr)

    arr = list(range(0, 30, 1))
    print("最初生成的arr: {}".format(arr))
    arr = [8, 2] + list(arr)
    random.shuffle(arr)
    # arr = arr[0: 10]
    print("【打乱顺序】最初的arr: {}".format(arr))

    # arr = arr[::-1]
    print("待处理的arr: {}".format(arr))

    for fun in [_01_bubble_sort_v1, _01_bubble_sort_v2, _02_selection_sort_v1, _03_insertion_sort_v1,  # 这3种性能同量级
                _04_shell_sort_v1, _05_merge_sort_v1, _06_quick_sort_v1, _06_quick_sort_v2, _07_heap_sort_v1,
                _07_heap_sort_v2, _07_heap_sort_v3,  # 这4种性能同量级
                _08_counting_sort_v1, _09_bucket_sort_v1, _10_radix_sort_v1, _10_radix_sort_v2]:  # 这3种性能同量级
    # for fun in [_07_heap_sort_v, _07_heap_sort_v1]:
    # for fun in [_04_shell_sort_v]:
    # for fun in [_09_bucket_sort_v1]:
        arr_tmp = arr[:]
        fun(arr_tmp)
        print()


if __name__ == "__main__":
    main()
