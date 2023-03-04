
from datascience import *
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def extract_rank(data,name):
    temp = data.where('姓名',are.equal_to(name)).column(11).item(0)
    return temp
    

data1 = Table.read_table('./bigdata_test/20211105-utf-8.csv')
data2 = Table.read_table('./bigdata_test/20211106-utf-8.csv')
data3 = Table.read_table('./bigdata_test/20211107-utf-8.csv')
data4 = Table.read_table('./bigdata_test/20211108-utf-8.csv')
data5 = Table.read_table('./bigdata_test/20211109-utf-8.csv')
data6 = Table.read_table('./bigdata_test/20211109-1-utf-8.csv')
data7 = Table.read_table('./bigdata_test/20211110-utf-8.csv')

name1 = input("请输入一个名字:")
name2 = input("请输入一个名字:")

rank1 = extract_rank(data1,name1)
rank2 = extract_rank(data2,name1)
rank3 = extract_rank(data3,name1)
rank4 = extract_rank(data4,name1)
rank5 = extract_rank(data5,name1)
rank6 = extract_rank(data6,name1)
rank7 = extract_rank(data7,name1)

rank8 = extract_rank(data1,name2)
rank9 = extract_rank(data2,name2)
rank10 = extract_rank(data3,name2)
rank11 = extract_rank(data4,name2)
rank12 = extract_rank(data5,name2)
rank13 = extract_rank(data6,name2)
rank14 = extract_rank(data7,name2)


rank_array = make_array(rank1,rank2,rank3,rank4,rank5,rank6,rank7)
rank_array2 = make_array(rank8,rank9,rank10,rank11,rank12,rank13,rank14)

results1 = Table().with_columns('考试序号',make_array(1,2,3,4,5,6,7),'姓名',rank_array)
results2 = Table().with_columns('考试序号',make_array(1,2,3,4,5,6,7),'姓名',rank_array2)
results1.show()
results2.show()

plt.plot(make_array(1,2,3,4,5,6,7),rank_array,'o--b',label=name1)
plt.plot(make_array(1,2,3,4,5,6,7),rank_array2,'o--r',label=name2)

plt.title(name1 +'和'+ name2 + '历次考试年级排名趋势图')
plt.xlabel('历次考试')
plt.ylabel('年级排名')

plt.axis([0,10,500,0])
plt.legend(loc='upper right')

plt.rcParams['font.sans-serif']=['Microsoft YaHei']

plt.grid()
plt.show()
请输入一个名字:刘翔
请输入一个名字:王凤仪
考试序号	姓名
1	76
2	187
3	334
4	222
5	131
6	97
7	457
考试序号	姓名
1	85
2	176
3	69
4	143
5	151
6	108
7	477
 
