
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from datascience import *

data1 = Table.read_table('./bigdata_test/20211105-utf-8.csv')
data2 = Table.read_table('./bigdata_test/20211106-utf-8.csv')
data3 = Table.read_table('./bigdata_test/20211107-utf-8.csv')
data4 = Table.read_table('./bigdata_test/20211108-utf-8.csv')
data5 = Table.read_table('./bigdata_test/20211109-utf-8.csv')
data6 = Table.read_table('./bigdata_test/20211109-1-utf-8.csv')
data7 = Table.read_table('./bigdata_test/20211110-utf-8.csv')

table = {}

def map(name,path):
    a = path.where('姓名',name)
    table[a.column(2).item(0)] = {'语文':a.column(3).item(0),'数学':a.column(4).item(0),'英语':a.column(5).item(0),'物理':a.column(6).item(0),'化学':a.column(7).item(0),'生物':a.column(8).item(0),'理综':a.column(9).item(0),'总分':a.column(10).item(0),}

for i in range(64):
    map(data1[2][i],data1)

for i in table.keys():
    a = data2.where('姓名',i)
    b = data3.where('姓名',i)
    c = data4.where('姓名',i)
    d = data5.where('姓名',i)
    e = data6.where('姓名',i)
    f = data7.where('姓名',i)
    
    table[i]['语文'] = table[i]['语文'] + a.column(3).item(0) + b.column(3).item(0) + c.column(3).item(0) + d.column(3).item(0) + e.column(3).item(0) + f.column(3).item(0)
    table[i]['数学'] = table[i]['数学'] + a.column(4).item(0) + b.column(4).item(0) + c.column(4).item(0) + d.column(4).item(0) + e.column(4).item(0) + f.column(4).item(0)
    table[i]['英语'] = table[i]['英语'] + a.column(5).item(0) + b.column(5).item(0) + c.column(5).item(0) + d.column(5).item(0) + e.column(5).item(0) + f.column(5).item(0)
    table[i]['物理'] = table[i]['物理'] + a.column(6).item(0) + b.column(6).item(0) + c.column(6).item(0) + d.column(6).item(0) + e.column(6).item(0) + f.column(6).item(0)
    table[i]['化学'] = table[i]['化学'] + a.column(7).item(0) + b.column(7).item(0) + c.column(7).item(0) + d.column(7).item(0) + e.column(7).item(0) + f.column(7).item(0)
    table[i]['生物'] = table[i]['生物'] + a.column(8).item(0) + b.column(8).item(0) + c.column(8).item(0) + d.column(8).item(0) + e.column(8).item(0) + f.column(8).item(0)
    table[i]['理综'] = table[i]['理综'] + a.column(9).item(0) + b.column(9).item(0) + c.column(9).item(0) + d.column(9).item(0) + e.column(9).item(0) + f.column(9).item(0)
    table[i]['总分'] = table[i]['总分'] + a.column(10).item(0) + b.column(10).item(0) + c.column(10).item(0) + d.column(10).item(0) + e.column(10).item(0) + f.column(10).item(0)
    
Chinese = []
Math = []
English = []
Physics = []
Chemistry = []
Creature = []
Straightforward = []
Sum = []
for i in table.keys():
    Chinese.append((i,table[i]['语文']))
    Math.append((i,table[i]['数学']))
    English.append((i,table[i]['英语']))
    Physics.append((i,table[i]['物理']))
    Chemistry.append((i,table[i]['化学']))
    Creature.append((i,table[i]['生物']))
    Straightforward.append((i, table[i]['理综']))
    Sum.append((i,table[i]['总分']))
    
Chinese_sort = sorted(Chinese, key=lambda x: x[1], reverse=True)[0:5]
Math_sort = sorted(Math, key=lambda x: x[1], reverse=True)[0:5]
English_sort = sorted(English, key=lambda x: x[1], reverse=True)[0:5]
Physics_sort = sorted(Physics, key=lambda x: x[1], reverse=True)[0:5]
Chemistry_sort = sorted(Chemistry, key=lambda x: x[1], reverse=True)[0:5]
Creature_sort = sorted(Creature, key=lambda x: x[1], reverse=True)[0:5]
Straightforward_sort = sorted(Straightforward, key=lambda x: x[1], reverse=True)[0:5]
Sum_sort= sorted(Sum, key=lambda x: x[1], reverse=True)[0:5]

Chinese_sort
    
[('何柃逸', 743), ('唐雯婕', 743), ('孙思', 719), ('刘欢', 716), ('唐杰', 715)]
Math_sort
[('王凤仪', 736), ('杨靖鑫', 661), ('陈文慧', 643), ('赵丹', 625), ('胥敏捷', 611)]
English_sort
[('唐杰', 729), ('张然', 728), ('潘虓虓', 710), ('黄思哲', 693), ('何柃逸', 685)]
Physics_sort
[('杨靖鑫', 491), ('刘翔', 486), ('王绍玮', 464), ('潘虓虓', 452), ('王宣', 450)]
Creature_sort
[('杨靖鑫', 476), ('王绍玮', 466), ('胥敏捷', 460), ('何柃逸', 455), ('王凤仪', 447)]
Straightforward_sort
[('刘翔', 1445), ('杨靖鑫', 1443), ('王绍玮', 1371), ('王宣', 1330), ('潘虓虓', 1305)]
Sum_sort
[('王凤仪', 3374), ('杨靖鑫', 3352), ('潘虓虓', 3284), ('刘翔', 3274), ('王绍玮', 3238)]
 
