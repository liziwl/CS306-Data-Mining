import numpy as np

a = np.array([[0, 0, 0, 0, 1],
              [1 / 3, 0, 0, 0, 0],
              [1 / 3, 0, 0, 0, 0],
              [1 / 3, 1 / 2, 0, 0, 0],
              [0, 1 / 2, 1, 1, 0]])
b = np.ones([5, 1]) / 5


def diff(old, new, range=0.0001):
    dif = np.abs(new - old)
    flag = np.dot(np.ones([1, dif.size]), dif)
    # print(flag)
    return flag < range


def page_iter(M, r, beta, size):
    t1 = np.dot(M * beta, r)
    t2 = np.ones([size, 1]) / size * (1 - beta)
    return t1 + t2


M = a
r_old = np.zeros_like(b)
r = b
i = 0
while not diff(r_old, r,1E-10):
    i += 1
    r_old = r
    r = page_iter(M, r_old, 0.8, r_old.size)
    # if i % 10 == 0:
    print("{} iteration:".format(i))
    print(r)

print(r)
