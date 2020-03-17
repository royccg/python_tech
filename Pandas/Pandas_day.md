<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [什么是Pandas](#什么是pandas)
- [Pandas数据读取](#pandas数据读取)
  - [代码演示： Pandas 读取数据](#代码演示-pandas-读取数据)
    - [读取纯文本](#读取纯文本)
- [Pandas数据结构：DataFrame & Series](#pandas数据结构dataframe-series)
    - [Series](#series)
    - [DataFrame](#dataframe)
- [Pandas数据查询：数值、列表、区间、条件、函数](#pandas数据查询数值-列表-区间-条件-函数)
  - [Pandas使用`df.loc`查询数据的方法](#pandas使用dfloc查询数据的方法)
    - [使用单个label值查询数据](#使用单个label值查询数据)
    - [使用值列表批量查询](#使用值列表批量查询)
    - [使用数值区间进行范围查询](#使用数值区间进行范围查询)
    - [使用条件表达式查询](#使用条件表达式查询)
    - [调用函数查询](#调用函数查询)

<!-- /code_chunk_output -->

#  什么是Pandas

一个开源的Python类库：用于数据分析、数据处理、数据可视化

* 高性能
* 容易使用的数据结构
* 容易使用的数据分析工具

很方便和其他类库一起使用：

* numpy：用于数学计算
* scikit-learn：用于机器学习

# Pandas数据读取

Pandas需要先读取<font color=red>表格类型</font>的数据，然后进行分析：

|   数据类型    |            说明             | pandas读取方法 |
| :-----------: | :-------------------------: | -------------- |
| csv、tsv、txt | 用逗号分隔、tab分隔的纯文本 | pd.read_csv    |
|     Excel     |     微软xls或者xlsx文件     | pd.read_excel  |
|     Mysql     |       关系型数据库表        | pd.read_sql    |

## 代码演示： Pandas 读取数据

本代码演示：
			1、pandas读取纯文本文件

* 读取csv文件

* 读取txt文件

  2、pandas读取xlsx格式文件

  3、pandas读取mysql数据表

```python
import pandas as pd
```



### 读取纯文本

--------

1、读取csv，使用默认的标题行、逗号分隔符

```python
fpath = './data/ml-latest-small/rating.csv'
# 使用pd.read_csv读取数据
ratings = pd.read_csv(fpath)
# 查看前几行数据
ratings.head()
# 查看数据的形状，返回（行数、列数）
ratings.shape
# 查看列名列表
ratings.colums
# 查看索引列
ratings.index
# 查看每列的数据类型
ratings.dtypes
```

2、读取txt文件、自己指定分隔符、列名

```python
fpath = './data/crayant/access_pvnv.txt'
pvnv = pd.read_csv(
	fpath,
  sep = "\t",
  header = None,
  # 设定列名
  names = ['pdata','pv','uv']
)
pvnv
```

3、读取excel文件

```python
fpath = './datas/crazyant/access_pvnv.xlsx'
pvnv = pd.read_excel(fpath)
pvnv
```

3、读取Mysql数据库

```python
import pymysql
conn = pymysql.connect(
	host = '127.0.0.1',
  user = 'root',
  password = '12345678',
  databas = 'test',
  charset = 'utf8'
	)
mysql_page = pd.read_sql('select * from crazyant_pvnv',con =conn)
mysql_page
```

# Pandas数据结构：DataFrame & Series

DataFrame：二维数据、整个表格，多行多列

Series：一维数据，一行或一列

```python
import pandas as pd
import numpy as np
```

### Series

Series是一种类似于一维数组的对象，它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成。

* 仅有数据列表即可产生最简单地Series

```python
s1 = pd.Series([1,'a',5.2,7])
# 左侧为索引，右侧是数据
s1
 0  1
 1  a
 2 5.2
 3  7
# 获取索引
s1.index
# 获取数据
s1.values
```



* 创建一个具有标签索引的Series

```python
s2 = pd.Series([1,'a',5.2,7],index = ['d','b','a','c'])
s2
  d      1
  b      a
  a     5.2
  c      7
  dtype:object
s2.index
 Index(['d','b','a','c'],dtype = 'object' )
```

* 使用Python字典创建Series

```python
sdata = {'Ohio':35000,'Texas':72000,'Orange':16000,'Utah':5000}
s3=pd.Series(sdata)
s3
	Ohio  35000
  ......
```

* 根据标签索引查询数据

类似Python的字典dict

```python
s2
	d    1
  b    a
  a    5.2
  c    7
  dtype:object
```

```python
s2['a']
   5.2
type(s2['a'])
	float
s2[['b','a']]
	b    a
  a    5.2
  dtype:object
type(s2[['b','a']])
	pandas.core.series.Series
```

### DataFrame

-------------------

DataFrame是一个表格型的数据结构

	* 每列可以是不同的值类型（数值、字符串、布尔值等）
	* 既有行索引index，也有列索引columns
	* 可以被看做由Series组成的字典

--------

- 根据多个字典序列创建dataframe
```Python
data = {
	'state':["Ohio",'Ohio','Ohio','Nevada','Nevada'],
	'year':[2000,2001,2002,2001,2002],
	'pop':[1.5,1.7,3.6,2.4,2.9]
}
df = pd.DataFrame(data)
```

```Python
df
```
| | state    | year  | pop |
|:------:| :-----------: | :-------------------------: | -------------- |
| 0|Ohio |2000 | 1.5 |
| 1|Ohio|2001 | 1.7 |
| 2|Ohio|2002 | 3.6|
| 3|Nevada|2001 |2.4 |
| 4|Nevada|2002 | 2.9 |

```python
df.dtype
	state  object
	year    int64
	pop     float64
	dtype:object

df.columns
	Index(['state','year','pop'],dtype='object')

df.index
	RangeIndex(start = 0,stop = 5,step =1)
```

- 从DataFrame中查询出Series
	- 如果只查询一列，返回的是pd.series
	- 如果查询多行、多列，返回的是 pd.dataframe
```python
#  查询单行
df.loc[1]
	state  Ohio
	year   2001
	pop     1.7
	Name:1,dtype :object

type(df.loc[1])
	pandas.core.series.Series

df.loc[1:3]
```

# Pandas数据查询：数值、列表、区间、条件、函数
----------------
	1、 df.loc 方法，根据行、列的标签值查询
	2、 df.iloc 方法，根据行、列的数字位置查询
	3、 df.where 方法
	4、 df.query 方法

	*。loc既能查询，又能覆盖写入，强烈推荐*

## Pandas使用`df.loc`查询数据的方法
--------
	1、 使用单个label值查询数据
	2、 使用值列表批量查询
	3、使用数值区间进行范围查询
	4、使用条件表达式查询
	5、调用函数查询


```yaml
注意：
	+ 以上查询方法，既适用于行，也适用于列
	+ 注意观察降维dataFrame>Series>值
```


```python
import pandas as pd
```
* 读取数据
数据为北京2018年全年天气预报

```python
df = pd.read_csv('beijing_tianqi_2018.csv')
df.head()
```

### 使用单个label值查询数据
-------------
行或者列，都可以只传入单个值，实现精确匹配

```python
#  得到单个值
df.loc['2018-01-03','bWendu']
	2
```
```python
# 得到一个Series
df.loc['2018-01-03',['bWendu','yWendu']]
	bWendu   2
	yWendu   -5
	Name:2018-01-03,dtype:object
```

### 使用值列表批量查询
```python
# 得到Series
df.loc[['2018-01-03','2018-01-04','2018-01-05'],'bWendu']
```


### 使用数值区间进行范围查询
注意：区间既包含开始，也包含结束
```python
# 行index按区间
df.loc['2018-01-03':'2018-01-05','bWendu':'fengxiang']
```

### 使用条件表达式查询
bool列表的长度得等于行数或者列数

+ 简单条件查询，最低温度低于-10度的列表
```python
df.loc[df['yWendu']<-10,:]
```

+ 复杂条件查询，查一下我心中的完美天气
注意，组合条件用& 符号合并，每个条件判断都得带括号

```python
#  查询最高温度小于30度，并且最低温度大于15度，并且是晴天，并且天气为优的数据
df.loc[(df['bWendu']<30) & (df['yWendu']>=15) & (df['tianqi']=='晴') & (df['aqiLevel'] ==1),:]
```

### 调用函数查询
```python
# 直接写lambda 表达式
	df.loc[lambda df:(df['bWendu']<=30 & df['yWendu']>=15),:]
```

```python
# 编写自己的函数，查询9月份，空气质量好的数据
def query_my_data(df):
	return df.index.str.startswith('2018-09') & df['aqiLevel'] ==1

df.loc[query_my_data,:]
```
