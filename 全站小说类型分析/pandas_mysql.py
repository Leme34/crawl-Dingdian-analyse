import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pymysql
import numpy as np

con=pymysql.connect(host='localhost',
                    user='root',
                    passwd='815211859',
                    db='xiaoshuo',
                    charset='utf8')
#df是DataFrame类型
df=pd.read_sql('SELECT * FROM dd_name',con)

#counts是Series类型
counts=df['category'].value_counts()

print(counts)

# 设置x，y轴刻度一致，这样饼图才能是圆的plt.axis('equal')
plt.axis('equal')
#legend就是添加图例的标注
# plt.legend()

#第一个参数：每个标签占比的列表
#labels:标签名字的列表
#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
#pctdistance，百分比的text离圆心的距离
#shadow，饼是否有阴影
#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
plt.pie(counts, labels = counts.keys(), autopct="%5.2f%%", pctdistance=0.6,
shadow=True, labeldistance=1.1, startangle=None, radius=None)

plt.savefig('C:/Users/Administrator.86NYOCTJWC9MW6J/Desktop/pandas/plot.png')
plt.show()


