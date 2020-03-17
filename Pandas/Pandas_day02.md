
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [05.Pandas新增数据列：直接赋值、apply、assign、分条件赋值](#05pandas新增数据列直接赋值-apply-assign-分条件赋值)
    - [读取csv数据到dataframe](#读取csv数据到dataframe)
    - [直接赋值的方法](#直接赋值的方法)
    - [df.apply方法](#dfapply方法)
    - [df.assign方法](#dfassign方法)
    - [按条件选择分组分别赋值](#按条件选择分组分别赋值)
- [06.Pandas数据统计函数](#06pandas数据统计函数)
  - [汇总类统计](#汇总类统计)
  - [唯一去重和按值计数](#唯一去重和按值计数)
    - [唯一性去重](#唯一性去重)
    - [按值计数](#按值计数)
    - [相关系数和协方差](#相关系数和协方差)
- [07.*Pandas缺失值处理*](#07pandas缺失值处理)
    - [步骤1:读取Excel的时候，忽略前几个空行](#步骤1读取excel的时候忽略前几个空行)
    - [步骤2：检测空值](#步骤2检测空值)
    - [删除掉全是空值得列](#删除掉全是空值得列)
    - [删除掉全是空值的行](#删除掉全是空值的行)
    - [步骤5：将分数列为空的填充为0分](#步骤5将分数列为空的填充为0分)
    - [步骤6：将姓名的缺失值填充](#步骤6将姓名的缺失值填充)
    - [步骤7：将清洗好的excel保存](#步骤7将清洗好的excel保存)
- [08.Pandas的SettingWithCopyWaring：报警复现、原因、解决方案](#08pandas的settingwithcopywaring报警复现-原因-解决方案)
  - [报警](#报警)
    - [0、读取数据](#0-读取数据)
    - [1.复现：有问题](#1复现有问题)
    - [2、原因](#2-原因)
    - [3、解决方法1](#3-解决方法1)
    - [4、解决方法2](#4-解决方法2)
- [09.Pandas数据排序](#09pandas数据排序)
    - [0、读取数据](#0-读取数据-1)
    - [1.Series的排序](#1series的排序)
    - [2、DataFrame的排序](#2-dataframe的排序)
    - [10.Pandas字符串](#10pandas字符串)
    - [1.获取Series的str属性，使用各种字符串处理函数](#1获取series的str属性使用各种字符串处理函数)
    - [2.使用str的startswith、contains等得到bool的Series可以做条件查询](#2使用str的startswith-contains等得到bool的series可以做条件查询)
    - [3.需要多次str处理的链式操作](#3需要多次str处理的链式操作)
    - [4.使用正则表达式的处理](#4使用正则表达式的处理)
- [11.Pandas的axis参数](#11pandas的axis参数)
    - [1、单列drop，就是删除某一列](#1-单列drop就是删除某一列)
    - [2、单行drop，就是删除某一行](#2-单行drop就是删除某一行)
    - [3、按axis =0/index执行mean聚合操作](#3-按axis-0index执行mean聚合操作)
    - [4、按axis=1/columns执行mean聚合操作](#4-按axis1columns执行mean聚合操作)
    - [5、再次举例，加深理解](#5-再次举例加深理解)

<!-- /code_chunk_output -->


# 05.Pandas新增数据列：直接赋值、apply、assign、分条件赋值
---------------
在进行数据分析时，经常要按照一定条件创建新的数据列，然后进行进一步的分析
* 直接赋值
* df.apply方法
* df.assign方法
* 按条件进行分组分别赋值
-----------------------------
`import pandas as pd`
### 读取csv数据到dataframe

```python
fpath = 'beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)
df.head()
```
### 直接赋值的方法
实例：清理温度列，变成数字类型
```python
df.loc[:,'bWendu'] = df["bWendu"].str.replace("C",'').astype('int32')
df.loc[:,'yWendu'] = df["yWendu"].str.replace("C",'').astype('int32')
```
实例：计算温差
```python
# 注意，df['bWendu']其实是一个Series，后面的减法返回的是Series
df.loc[:,"wencha"] = df['bWendu']-df['yWendu']
```

### df.apply方法
Apply a function along an axis of the DataFrame.
Objects passed to the function are Series objects whose index is either the DataFrame's index (axis = 0) or the DataFrame's columns(axis = 1).

实例：添加一列温度类型：
	1、如果最高温度大于33摄氏度就是高温
	2、低于-10摄氏度就是低温
	3、否则就是常温

```python
	def get_wendu_type(x):
		if x['bWendu'] > 33:
			return "高温"
		elif x["yWendu"] < -10:
			return '低温'
		else:
			return "常温"

	# 注意需要设置axis = 1，这是Series的index是columns
	df.loc[:,"wendu_type"] = df.apply(get_wendu_type,axis = 1)

	df['wendu_type'].value_counts()
```
### df.assign方法
Assign new columns to a DataFrame.
Returns a new object with all orignal columns in addition to new ones.
实例：将温度从摄氏度变成华氏度
```python
# 可以同时添加多个新的列
df.assign(
  yWendu_huashi = lambda x: x['yWendu'] * 9/5 + 32,
  # 摄氏度转变为华氏度
  bWendu_huashi = lambda x: x['bWendu'] * 9/5 + 32
)
```
### 按条件选择分组分别赋值
按条件先选择数据，然后对这部分数据赋值新列
实例：高低温差大于10度，则认为温差大
```python
df['wencha_type'] = ''
df.loc[df['bWendu']-df['yWendu']>10,'wencha_type'] = '温差大'
df.loc[df['bWendu']-df['yWendu']<=10,'wencha_type'] = '温差正常'

df['wencha_type'].value_counts()
```

# 06.Pandas数据统计函数
-----------------

主要内容：
  1、汇总类统计
  2、唯一去重和按值计数
  3、相关系数和协方差

-------------
```python
import pandas as pd
```

## 汇总类统计
```python
# 一下子提取所有数字列统计结果
df.describe()

# 查看单个Series的数据
df['bWendu'].mean()
# 最高温
df['bWendu'].max()
# 最低温
df['bWendu'].min()
```

## 唯一去重和按值计数
### 唯一性去重
一般不用于数值列，而是枚举、分类列
```python
df['fengxiang'].unique()
df['tianqi'].unique()
df['fengli'].unique()
```

### 按值计数
```python
df['fengxiang'].value_counts()
df['tianqi'].value_counts()
df['fengli'].value_counts()
```

### 相关系数和协方差
用途（超级厉害）：
  1.两只股票，是不是同涨同跌？程度多大？正相关还是负相关？
  2.产品销量的波动，跟哪些因素正相关、负相关，程度有多大？
来自知乎：
  1.协方差：***衡量同向反向程度***，如果协方差为正，说明X、Y同向运动，协方差越大说明同向程度越高；如果协方差为负，说明X、Y反向运动，协方差越小说明反向程度越高。
  2.相关系数：***衡量相似程度***，当他们的相关系数为1时，说明两个变量变化时的正向相似度最大，当相关系数为-1时，说明两个变量变化的反向相识度最大。

```python
# 协方差矩阵
df.cov()

# 相关系数矩阵
df.corr()

# 单独查看空气质量和最高温度的相关系数
df['aqi'].corr(df['bWendu'])
df['aqi'].corr(df['yWendu'])

# 空气质量和温差的相关系数
df['aqi'].corr(df['bWendu']-df['yWendu'])
# !!这就是特征工程对于机器学习重要性的一个例子
```

# 07.*Pandas缺失值处理*
----------------
Pandas使用这些函数处理缺失值：
* isnull和nonull：检测是否是空值，可用于df和Series
* dropna:丢失、删除缺失值
  * axis：删除行还是列，{0 or 'index',1 or 'columns'},default 0
  * how：如果等于any则任何值为空都删除，如果等于all则所有值都为空才删除
  * inplace:如果为True则修改当前df,否则返回新的df
* fillna:填充空值
  * value：用于填充的值，可以是单个值，或者字典（key是列名，value是值）
  * method：等于ffill使用前一个不为空的值填充forword fill;等于bfill使用后一个不为空的值填充backword fill.
  *   axis：按行还是列填充，{0 or 'index',1 or 'columns'}
  *   inplace：如果为True则修改当前df,否则返回新的df
```python
import pandas as pd
```
实例：特殊Excel的读取、清洗、处理
### 步骤1:读取Excel的时候，忽略前几个空行
```python
studf = pd.read_excel('student_excel.xlsx',skiprows = 2)
# 忽略前两行
```

### 步骤2：检测空值
```python
studf.isnull()
# 空值 会返回 True

studf['分数'].isnull()
studf['分数'].notnull()
# 筛选没有空分数的所有行
studf.loc[studf['分数'].notnull(),:]
```

### 删除掉全是空值得列
```python
# 删除掉all全是空值的列
studf.dropna(axis = 'columns',how = 'all',inplace = True)
```

### 删除掉全是空值的行
```python
studf.dropna(axis = 'index',how = 'all',inplace = True)
```

### 步骤5：将分数列为空的填充为0分
```python
studf.fillna({'分数':0})

# 等同于
studf.loc[:,'分数'] =studf['分数'].fillna(0)
```

### 步骤6：将姓名的缺失值填充
使用前面的有效值填充，用ffill:forward fill
```python
studf.loc[:,'姓名'] =studf['姓名'].fillna(method = 'ffill')
```

### 步骤7：将清洗好的excel保存
```python
studf.to_excel('student_excel_clean.xlsx',index = False)
```


# 08.Pandas的SettingWithCopyWaring：报警复现、原因、解决方案
---------------
## 报警
### 0、读取数据
```python
import pandas as pd
fpath = 'beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)

# 替换掉温度的后缀 ℃
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')
```

### 1.复现：有问题
```python
# 只选出3月份的数据用于分析
condition = df['ymd'].str.startswith('2018-03')
# 设置温差
df[condition]['wen_cha'] = df['bWendu']-df['yWendu']
# 查看是否修改成功
df[condition].head()
```

### 2、原因
发出警告的代码 df[condition]['wen_cha'] = df['bWendu']-df['yWendu']
相当于：df.get(condition).set(wen_cha),第一步骤的get发出了报警
***链式操作其实是两个步骤，先get后set，get得到的dataframe可能是view也可能是copy，pandas发出警告***
官网文档：https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

核心要诀：pandas的dataframe的修改写操作，只允许在源dataframe上进行，一步到位

### 3、解决方法1
将get+set的两步操作，改成set的一步操作
```python
df.loc[condition,'wen_cha']=df['bWendu']-df['yWendu']
df[condition].head()
```
### 4、解决方法2
如果需要预筛选数据做后续的处理分析，使用copy复制dataframe
```python
df_month3 = df[condition].copy()
df_month3.head()
df_month3['wen_cha'] = df['bWendu'] - df['yWendu']
df_month3.head()
```
***总之，pandas不允许先筛选子dataframe，再进行修改写入***
要么使用```.loc```实现一个步骤直接修改源dataframe
要么先复制一个子dataframe再一个步骤执行修改

# 09.Pandas数据排序
----------
Series的排序：
```python
Series.sort_values(ascending=True,inplace = False)
```
参数说明：
  * ascending:默认为True升序排列，为False降序排序
  * inplace：是否修改原始Series
DataFrame的排序：
```python
DataFrame.sort_values(by,ascending = True,inplace = False)
```
参数说明：
  * by:字符串或者List<字符串>,单列排序或者多列排序
  * ascending:bool或者List，升序还是降序，如果是list对应by的多列
  * inplace：是否修改原始DataFrame

```python
import pandas as pd
```

### 0、读取数据
```python
fpath = 'beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)

# 替换掉温度的后缀℃
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')
df.head()
```

### 1.Series的排序
```python
df['aqi'].sort_values()
df['aqi'].sort_values(ascending = False)
df['tianqi'].sort_values()
```

### 2、DataFrame的排序
* 单列排序
  ```python
  df.sort_values(by = 'aqi')
  df.sort_values(by = 'aqi', ascending = False)
  ```
* 多列排序
  ```python
  #  按空气质量等级、最高温度排序，默认升序
  df.sort_values(by = ['aqiLevel','bWendu'])
  # 两个字段都是降序
  df.sort_values(by = ['aqiLevel','bWendu'],ascending = False)
  # 分别指定升序和降序
  df.sort_values(by = ['aqiLevel','bWendu'],ascending = [True,False])
  ```

### 10.Pandas字符串
--------------------
前面我们已经使用了字符串的处理函数：
```python
df['bWendu'].str.replace('℃','').astype('int32')
```
***Pandas的字符串处理***
  1. 使用方法：先获取Series的str属性，然后在属性上调用函数；
  2. 只能在字符串列上使用，不能数字列上使用；
  3. DataFrame上没有str属性和处理方法；
  4. Series.str并不是Python原生字符串，而是自己的一套方法，不过大部分的原生str很相似；
Series.str字符串方法列表参考文档：
  https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handing
本节演示内容：
  * 获取Series的str属性，然后使用各种字符串
  * 使用str的startswith、contains等bool类Series可以做条件查询
  * 需要多次str处理的链式操作
  * 使用正则表达式的处理

  ### 0.读取北京2018年天气数据
  ```Python
  import pandas as pd
  fpath = 'beijing_tianqi_2018.csv'
  df = pd.read_csv(fpath)
  df.head()
  df.dtypes
  ```

### 1.获取Series的str属性，使用各种字符串处理函数
```python
df['bWendu'].str
# 字符串替换函数
df['bWendu'].str.replace('℃','')
# 判断是不是数学
df['bWendu'].str.isnumeric()
df['sqi'].str.len()
```

### 2.使用str的startswith、contains等得到bool的Series可以做条件查询
```python
condition = df['ymd'].str.startswith('2018-03')
df[condition].head()
```

### 3.需要多次str处理的链式操作
怎样提取201803这样的数字月份？
  * 先将日期2018-03-31替换成20180331的形式
  * 提取月份字符串201803
```python
df['ymd'].str.replace('-','')
# 每次调用函数，都返回一个新的Series
df['ymd'].str.replace('-','').slice(0,6) # 报错
df['ymd'].str.replace('-','').str.slice(0,6)
# slice就是切片语法，可以直接用
df['ymd'].str.replace('-','').str[0:6]
```

### 4.使用正则表达式的处理
```python
# 添加新列
def get_nianyueri(x):
  year.month.day = x['ymd'].split('-')
  return f'(year)年(month)月(day)日'
df['中文日期'] = df.apply(get_nianyueri,axis = 1)
```
问题：怎样将‘2018年12月31日’中的年、月、日三个中文字符去除？
```python
# 方法1：链式replace
df['中文日期'].str.replace('年','').str.replace('月','').str.replace('日','')
```
***Series.str默认就开启了正则表达式模式***
```python
# 方法2：正则表达式替换
df['中文日期'].str.replace('[年月日]','')
```

# 11.Pandas的axis参数
--------------------------
* axis = 0 或者 ‘index’：
  * 如果是单行操作，就指的是某一行
  * 如果是聚合操作，指的是跨行cross rows
* axis = 1 或者 'columns':
  * 如果是单列操作，就指的是某一列
  * 如果是聚合操作，指的是跨列cross columns

***按哪个axis，就是这个axis要动起来（类似被for遍历），其它的axis保持不动***
```python
import pandas as pd
import numpy as np
```

```python
df = pd.DataFrame(
  np.arange(12).reshape(3,4),
  columns = ['A','B','C','D']
  )
```
### 1、单列drop，就是删除某一列
```python
# 代表的就是删除某列
df.drop('A',axis =1)
```
### 2、单行drop，就是删除某一行
```python
df.drop(1,axis = 0)
```

### 3、按axis =0/index执行mean聚合操作
反直觉：输出的不是每行的结果，而是每列的结果
```python
# axis = 0 or axis =index
df.mean(axis = 0)
```

### 4、按axis=1/columns执行mean聚合操作
反直觉：***输出的不是每行的结果，而是每列的结果***
```python
# axis = 1 or axis = columns
df.mean(axis = 1)
```
***指定了按哪个axis，就是这个axis要动起来（类似被for遍历），其余的axis保持不动***

### 5、再次举例，加深理解
```python
def get_sum_value(x):
  return x['A']+x['B']+x["C"]+x['D']
df['sum_value'] =df.apply(get_sum_value,axis = 1)
```

***指定了按哪个axis，就是这个axis要动起来（类似被for遍历），其它的axis保持不动***
