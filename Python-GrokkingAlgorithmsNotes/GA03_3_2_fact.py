# -*- coding: UTF-8 -*-

# 《算法图解》第三章·递归 P36 累乘/累加

# 递归 累乘
def fact_01(x):
    if x == 1:
        return 1
    else:
        return x * fact_01(x-1)

# 递归 累加
def fact_02(x):
    if x == 0:
        return 0
    else:
        return x + fact_02(x-1)

print "累乘 " + str(fact_01(5))
print "累加 " + str(fact_02(5))
