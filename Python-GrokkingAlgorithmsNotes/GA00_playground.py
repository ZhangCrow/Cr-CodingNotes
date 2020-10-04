# -*- coding: UTF-8 -*-

'''
——————————————————————————
 GA00_playground
《算法图解》笔记 - 临时代码板
——————————————————————————
'''


# 《算法图解》第八章·贪婪算法 P121 集合覆盖问题
# 寻找尽量少的电台覆盖全国各地

# 需要覆盖的各地区
states_needed = set(["京", "津", "冀", "江", "浙", "沪", "豫", "鲁"])

# 可供选择的广播台清单
stations = {}
stations["key-1"] = set(["江", "浙", "沪"])
stations["key-2"] = set(["津", "江", "京"])
stations["key-3"] = set(["冀", "浙", "豫"])
stations["key-4"] = set(["浙", "沪"])
stations["key-5"] = set(["豫", "鲁"])

# 最终选择的广播台
final_stations= set()

while states_needed:
    # 当前步骤最合适的台及其覆盖的地区 局部最优解
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # 计算交集
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
    
print final_stations

