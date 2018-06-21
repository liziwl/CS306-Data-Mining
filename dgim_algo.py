# coding: utf-8

import numpy as np
import random as ra


# Q1: 假定采用上图窗口，试着分别估计当k=5及15时最后k位中1的个数，并给出两个估计结果与真实值的差值。
# Q2: 给出上图中还有3个1到达窗口的变化情况，可以假设图中所有的1都不离开窗口。
def real_last_k(k, arr):
    if k > len(arr):
        raise IndexError()
    count = 0
    for i in range(len(arr) - 1, len(arr) - 1 - k, -1):
        if arr[i] == 1:
            count += 1
    return count


def est_last_k(k, arr):
    buck = build_bucket(arr)
    lev = 1
    count = 0
    flag = True
    last = None
    while flag:
        tmp = buck[lev]
        for i in range(len(tmp) - 1, -1, -1):
            if count + lev <= k:
                last = (lev, i)
                count += lev
            else:
                flag = False
                break
        lev = lev * 2

    # print(last)
    lev = 1
    count = 0
    while True:
        if lev < last[0]:
            count += len(buck[lev]) * lev
        elif lev == last[0]:
            for i in range(len(buck[lev]) - 1, -1, -1):
                if i > last[1]:
                    count += lev
                elif i == last[1]:
                    count += lev / 2
                else:
                    break
        else:
            break
        lev = lev * 2
    return int(count)


def build_bucket(arr):
    buck = dict()
    for i in range(len(arr)):
        buck = update_bucket(arr[i], buck)
    # print(buck)
    return buck


def update_bucket(item, buck):
    if item == 0:
        buck[1][-1].append(item)
    else:
        index = 1
        tmp = [item, ]
        while True:
            # print(buck)
            if index not in buck:
                buck[index] = list()
            buck[index].append(tmp)
            if len(buck[index]) > 2:
                tmp = buck[index][0] + buck[index][1]
                del buck[index][0]
                del buck[index][0]
                index = index * 2
            else:
                break
    return buck


if __name__ == '__main__':
    hist = [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]

    print("真实值", real_last_k(10, hist))
    print("估计值", est_last_k(10, hist))

    buck = build_bucket(hist)
    print("插入前\t", buck)
    for i in range(3):
        print("插入1\t", update_bucket(1, buck))
