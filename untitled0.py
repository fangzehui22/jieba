import jieba
import collections
s="制作一个购票小程序，这个购票小程序可以根据客户曾经的购票历史"
s+="和评分记录自动推荐用户感兴趣的内容以及热门的热点项"
s+="目，类似于大数据的推荐系统。"
s1=jieba.cut(s)
k=[]
l=['、','，','。','；','！']
for i in s1:
    if i not in l:
        k.append(i)
count=collections.Counter(k)
for a,b in count.most_common():
    print(a,b)
