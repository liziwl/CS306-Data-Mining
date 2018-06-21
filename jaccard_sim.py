# coding: utf-8

import numpy as np
import random as ra

set1 = {'a', 'd'}
set2 = {'c'}
set3 = {'b', 'd', 'e'}
set4 = {'a', 'c', 'd'}
sets = [set1, set2, set3, set4]


# question 1
def jaccard(set_a, set_b):
    inter = set_a & set_b
    union = set_a | set_b
    return len(inter) / len(union)


print(jaccard(set4, set3))


# question 2.1
def bool_mat(set_list):
    union = set()
    for s in set_list:
        union = union | s
    arr = list(union)
    arr.sort()
    # print(arr)
    data = np.zeros((len(arr), len(sets)))
    for i in range(len(sets)):
        s = sets[i]
        for item in s:
            data[arr.index(item)][i] = 1
    return data


data = bool_mat(sets)
print(data)


# question 2.2
def min_hash(arr):
    length = len(arr[0])
    rand = list(range(1, length + 1))
    ra.shuffle(rand)
    hash_arr = [-1 for i in range(length)]
    count = length
    for i in range(length):
        tmp = arr[rand.index(i + 1)]
        for j in range(len(tmp)):
            if count <= 0:
                break
            if tmp[j] == 1 and hash_arr[j] == -1:
                hash_arr[j] = i + 1
                count -= 1
        if count <= 0:
            break
    return hash_arr


print(min_hash(data))


# question 2.3
def same_hash(arr, index_a, index_b, rate=10000):
    inter = 0
    for i in range(rate):
        sample = min_hash(arr)
        if sample[index_a] == sample[index_b]:
            inter += 1
    print(inter / rate)


same_hash(data, 2, 3)

# question 3.1
mat = [
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 0]
]
func1 = "(2*{}+1)%6"
func2 = "(3*{}+2)%6"
func3 = "(5*{}+2)%6"
func = [func1, func2, func3]
def min_hash_sig(func_list, matrix):
    out = np.zeros((len(func), len(matrix[0])))
    out.fill(np.inf)
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if matrix[j][i] == 1:
                for k in range(len(func)):
                    out[k][i] = min(out[k][i], eval(func[k].format(j)))
    return out


sig = min_hash_sig(func, mat)
print(sig)


# question 4.1

def get_prob(r, b):
    print("r: {} b: {}".format(r, b))
    print("s\t\tprob.")
    s = [i / 10 for i in range(0, 10)]
    form = "1-(1-{}**{})**{}"
    for si in s:
        print("{}:\t{}".format(si, eval(form.format(si, r, b))))


get_prob(3, 10)
get_prob(6, 20)
get_prob(5, 50)


def threshold(r, b):
    return eval("(1/{})**(1/{})".format(b, r))


thr = []
thr.append(threshold(3, 10))
thr.append(threshold(6, 20))
thr.append(threshold(5, 50))


def prob5(r, b):
    error = 1e-5
    form = "1-(1-{}**{})**{}"
    val = [0, 1]
    while (val[1] - val[0] > error):
        mid = (val[1] + val[0]) / 2
        if eval(form.format(mid, r, b)) < 0.5:
            val[0] = mid
        else:
            val[1] = mid
    return (val[1] + val[0]) / 2


prob = []
print("--------------------------")
prob.append(prob5(3, 10))
prob.append(prob5(6, 20))
prob.append(prob5(5, 50))

print("threshold", thr)
print("prob. 0.5", prob)

