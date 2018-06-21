# coding: utf-8

import numpy as np
import random as ra


# Q1: 计算流3,1,4,1,3,4,2,1,2的奇异数（二阶矩）。这个流的三阶矩是什么？
def count_freq(data):
    count = dict()
    for i in data:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


def surprise_number(data):
    count = count_freq(data)
    num = 0
    for i in count:
        num += count[i] ** 2
    # print(num)
    return num


def third_moment(data):
    count = count_freq(data)
    num = 0
    for i in count:
        num += count[i] ** 3
    # print(num)
    return num


# Q2: 假设我们得到流3,1,4,1,3,4,2,1,2，我们应用AMS算法来估计奇异数。
# 对于每个的可能值i，𝑋_𝑖表示起始位置为i的变量，那么每个𝑋_𝑖.value的值分别是多少？

def est_surprise_num(data):
    x = [0 for i in range(len(data))]
    next = dict()
    for i in range(len(data) - 1, -1, -1):
        if data[i] not in next:
            next[data[i]] = i
            x[i] = 1
        else:
            x[i] = x[next[data[i]]] + 1
            next[data[i]] = i
    return x


if __name__ == '__main__':
    data = [3, 1, 4, 1, 3, 4, 2, 1, 2]
    print("二阶矩", surprise_number(data))
    print("三阶矩", third_moment(data))
    print(est_surprise_num(data))
