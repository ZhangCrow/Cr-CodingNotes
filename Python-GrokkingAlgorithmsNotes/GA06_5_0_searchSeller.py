# -*- coding: UTF-8 -*-

# 《算法图解》第六章·广度优先搜索 P84 广度优先搜索-队列-有向图
# 广度优先搜素 - 队列 - 有向图
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

def search(name):
    # 创建一个队列
    search_queue = deque()
    # 将你的邻居都加入到这个搜索队列中
    search_queue += graph[name]
    # 这个数组用于记录检查过的人
    searched = []

    # 只要对列不为空
    while search_queue:
        # 就取出其中的第一个人
        person = search_queue.popleft()
        # 仅当这个人没检查过时才检查
        if person not in searched:
            # 检查这个人是不是销售商
            if person_is_seller(person):
                print person + "是销售商"
                return True
            else:
                # 不是销售商 则将这个人的朋友都加入搜索队列
                search_queue += graph[person]
                searched.append(person)
    # 如果执行到这里 就说明队列中没人是销售商
    print "人脉中没有销售商"
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search("you")
