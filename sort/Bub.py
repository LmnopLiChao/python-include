'''
Created on 2018年5月30日

@author: lichao
'''
#冒泡排序
def buble(bub):
    l = len(bub)
    for i in range(l-1):
        for j in range(l-i-1):
            if bub[j]>bub[j+1]:
                bub[j], bub[j + 1] = bub[j + 1], bub[j]
    return bub
#选择排序
def selection(sel):
    l = len(sel)
    for i in range(0, l-1):
        min_ = i
        for j in range(i + 1, l):
            if sel[j] < sel[min_]:
                min_ = j
        sel[i], sel[min_] = sel[min_], sel[i]  # swap
    return sel