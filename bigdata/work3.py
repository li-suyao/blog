from datascience import *

import pandas as pd

a1 = pd.read_csv('hadoop.csv')

a2 = pd.read_csv('hive.csv')

a3 = pd.read_csv('math.csv')

a4 = pd.read_csv('spark.csv')

result=pd.concat([a1,a2,a3,a4])

result.to_csv("jiankaobiao.csv",encoding='utf-8')

jiankao=Table.read_table('jiankaobiao.csv')

who_cource=jiankao.where('姓名',are.equal_to('李素瑶'))

print(who_cource)
=================== RESTART: D:\wenjian\云计算\jiankao\test2.py ===================
Unnamed: 0 | 学号         | 姓名   | 日期         | 时间          | 教室     | 科目
4          | 2020145109 | 李素瑶  | 2022/11/14 | 14:30-16:30 | 教二109  | hadoop
10         | 2020145109 | 李素瑶  | 2022/11/14 | 8:30-10:30  | 教二109  | 高数
10         | 2020145109 | 李素瑶  | 2022/11/15 | 8:30-10:30  | 理一B208 | spark
