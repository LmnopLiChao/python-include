#!/usr/local/bin/python3.6
# encoding: utf-8
from numpy import *
import operator

def creatDataSet ():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','B','C','D']
    return group,labels
'''
inx 传入的目标节点
dataSet 源数据字典
labels  对应节点名称
k 需要匹配的数据字典长度  不能超过字典长
'''
def classify0(inx,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx,(dataSetSize,1)) - dataSet
    sqlDiffMat = diffMat**2
    squareDist = sqlDiffMat.sum(axis = 1)###行向量分别相加，从而得到新的一个行向量
    dist = squareDist ** 0.5
    ##对距离进行排序
    sortedDistIndicies = dist.argsort()##argsort()根据元素的值从大到小对元素进行排序，返回下标
    classCount ={}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        ###对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]