# coding: utf-8

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def gen_DAG(G, src):
    D = nx.DiGraph()
    cur = [src, ]
    visited = set()
    while len(cur) > 0:
        next_tmp = set()
        visited = visited | set(cur)
        for i in cur:
            next_tmp = next_tmp | set(G.neighbors(i))
        next_tmp = next_tmp - visited
        for i in cur:
            nei = G.neighbors(i)
            for n in nei:
                if n in next_tmp:
                    # print("{}->{}".format(i, n))
                    D.add_edge(i, n)
        cur = list(next_tmp)
    return D


def calc_path(G, G_dag, src, recursive=False):
    child = list(G.successors(src))
    if len(child) == 0:
        return 1 / len(G_dag[src])
    sum = 0
    for i in child:
        sum += calc_path(G, G_dag, i, True)
    if recursive:
        return (sum + 1) / len(G_dag[src])
    else:
        return sum


G = nx.Graph()
G.add_nodes_from([i for i in range(1, 11)])
G.add_edges_from([(1, 4), (1, 5), (1, 6), (4, 8), (4, 3), (5, 3), (5, 7), (6, 2), (3, 7), (7, 2), (7, 10), (9, 2)])

# 网络图
nx.draw(G,with_labels = True)
plt.show()

# Question 1
#                              1
#                            / | \
#                           4  5  6
#                         / | /|  |
#                        /  |/ |  |
#                       8   3--7--2
#                              |  |
#                             10  9
# 上图为一个社会网络图的例子。利用GN算法寻找从以下节点开始经过每条边的最短路径的数目
# 节点1，节点2

D1 = gen_DAG(G, 1)
# 处理过的层次网络图，去掉了同层的边，变成了有向图
nx.draw(D1, with_labels=True)
plt.show()

dag = nx.predecessor(D1, 1)
print(calc_path(D1, dag, 1))

D2 = gen_DAG(G, 2)
# 处理过的层次网络图，去掉了同层的边，变成了有向图
nx.draw(D2, with_labels=True)
plt.show()

dag = nx.predecessor(D2, 2)
print(calc_path(D2, dag, 2))
