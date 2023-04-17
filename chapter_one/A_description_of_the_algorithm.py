# __*__coding: utf-8
# @Time : 2023/4/17 
# @ Author :lvlongxin
# @File : A_description_of_the_algorithm
# @Prooject : algorithm_my
def lvlongxin() -> int:
    print("ppp")
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

"""
循环体内会循环执行n次，循环语句，如果每次执行语句的时间是x，共耗时nx
res = 0  和 return res 分别耗时是 y 和 z  
那么总耗时是 nx + y + z
如果x，y，z耗时相等的话。总耗时是：(n + 2)x
随着数据量的增大，耗时会不断趋近于 nx
这个就是这个程序的时间复杂度
"""