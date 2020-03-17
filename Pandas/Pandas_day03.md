
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [12.Pandas的索引index](#12pandas的索引index)
  - [1.使用index查询数据](#1使用index查询数据)
  - [2.使用index会提升查询性能](#2使用index会提升查询性能)
    - [实验1：完全随机的顺序查询](#实验1完全随机的顺序查询)
    - [实验2：将index排序后的查询](#实验2将index排序后的查询)
  - [3.使用index能自动对齐数据](#3使用index能自动对齐数据)
  - [4.使用index更多更强大的数据结构支持](#4使用index更多更强大的数据结构支持)

<!-- /code_chunk_output -->


# 12.Pandas的索引index
------------------
把数据储存于普通的column列也能用于数据查询，那使用index有什么好处？
index的用途总结：
    1. 更方便的数据查询；
    2. 使用index可以获得性能提升；
    3. 自动的数据对齐功能；
    4. 更多更强大的数据结构支持；

```python
import pandas as pd
df = pd.read_csv('rating.csv')
df.head()
df.count()
```

## 1.使用index查询数据
```python
# drop-False,让索引列还保持在column
df.set_index('userId',inplace =True,drop =False)
df.head()
df.index

# 使用index的查询方法
df.loc[500].head(5)
# 使用column的condition 查询方法
df.loc[df['userId'] == 500].head()
```

## 2.使用index会提升查询性能
* 如果index是唯一的，Pandas会使用哈希表优化，查询性能为O(1);
* 如果index不是唯一的，但是有序，Pandas会使用二分查找算法，查询性能为O(logN);
* 如果index是完全随机的，那么每次查询都要扫描全表，查询性能O(N);

### 实验1：完全随机的顺序查询
```python
# 将数据随机打散
from sklearn.utils import shuffle
df_shuffle = shuffle(df)
df_shuffle.head()

# 索引是否是递增的
df_shuffle.index.is_monotonic_increasing
df_shuffle.index.is_unique
# 计时，查询id = 500数据性能
%timeit df_shuffle.loc[500]
```

### 实验2：将index排序后的查询
```python
df_sorted = df_shuffle.sort_index()
df_sorted.head()
# 索引是否是递增的
df_sorted.index.is_monotonic_increasing
df_sorted.index.is_unique
```

## 3.使用index能自动对齐数据
包括series和dataframe
```python
s1 = pd.Series([1,2,3],index = list('abc'))
s2 = pd.Series([2,3,4],index = list('bcd'))
s1+s2
```

## 4.使用index更多更强大的数据结构支持
***很多强大的索引数据结构***
  * CategoricalIndex，给予分类数据的Index，提升性能；
  * Multilndex，多维索引，用于groupby多维聚合后结果等；
  * DatetimeIndex，时间类型索引，强大的日期和时间的方法支持；
