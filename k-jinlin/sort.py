# encoding: utf-8
import kNN

group,labels = kNN.creatDataSet()
print(kNN.classify0([1,0],group,labels,3))
