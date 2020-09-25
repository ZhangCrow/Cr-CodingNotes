# -*- coding: UTF-8 -*-

# 《算法图解》第七章·狄克斯特拉算法 P108 不含负权边的有向无环图-寻找最快路径
# 狄克斯特拉算法 - 不含负权边的有向无环图
# 寻找最快路径
# 定义一个散列表/字典 来构建带权重的有向图

start = "start"
a = "a"
b = "b"
finish = "finish"

graph = {}
graph[start] = {}
graph[start][a] = 6
graph[start][b] = 2
print graph[start].keys()
print graph[start][a]
print graph[start][b]

graph[a] = {}
graph[a][finish] = 1

graph[b] = {}
graph[b][a] = 3
graph[b][finish] = 5

graph[finish] = {}

# 定义一个散列表 存储每个节点的开销（从起点至该节点的权重）
infinity = float("inf")
costs = {}
costs[a] = 6
costs[b] = 2
costs[finish] = infinity

# 定义一个散列表 存储每个节点的父节点
parents = {}
parents[a] = start
parents[b] = start
parents[finish] = None

# 定义一个数组 记录处理过的节点
processed = []

# 准备工作完毕
# 实现狄克斯特拉算法

# 查找当前开销最低的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # 遍历所有的节点
    for node in costs:
        cost = costs[node]
        # 如果当前节点的开销更低 且 未被处理过
        if cost < lowest_cost and node not in processed:
            # 就视其为开销最低的节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
# 这个while循环在所有节点都被处理过后结束
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历当前节点的所有邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 如果经当前节点前往该邻居更近
        if costs[n] > new_cost:
            # 就更新该邻居的开销
            costs[n] = new_cost
            # 同时将该邻居的父节点设置为当前节点
            parents[n] = node
    # 将当前节点标记为已处理过
    processed.append(node)
    # 找出接下来要处理的节点 并循环
    node = find_lowest_cost_node(costs)

print graph
print parents
print costs
