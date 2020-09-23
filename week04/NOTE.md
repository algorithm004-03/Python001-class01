第四周学习笔记

# 作业记录

1. pandas使用及matplotlib使用要继续实践熟悉。
2. jieba分词部分分词需关闭自动词频后及手动调整词频配合使用需再测试测试。

# 1. pandas简介

**说明：**19 分 54 秒处的 `df[1:3]` 应该是 `df[0:3]` ，这里的原理和 Python 数组的切片是一样的。

**1. 获取课程源码操作方法：**

切换分支：git checkout 4a

**2. pandas 中文文档：**

[https://www.pypandas.cn/](https://www.pypandas.cn/)

sklearn-pandas

**3. 安装参考文档：**

[https://pypi.org/project/sklearn-pandas/1.5.0/](https://pypi.org/project/sklearn-pandas/1.5.0/)

**4. Numpy 学习文档：**

[https://numpy.org/doc/](https://numpy.org/doc/)

**5. matplotlib 学习文档：**

[https://matplotlib.org/contents.html](https://matplotlib.org/contents.html) 

# 2. pandas基本数据类型

**1. 获取课程源码操作方法：**

切换分支：git checkout 4a

# 3. pandas数据导入

1. 获取课程源码操作方法：

切换分支：git checkout 4a

# 4. pandas数据预处理

**1. 获取课程源码操作方法：**

切换分支：git checkout 4b

**2. Series 学习文档：**

[https://pandas.pydata.org/pandas-docs/stable/reference/series.html](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

# 5. pandas数据调整

**1. 获取课程源码操作方法：**

切换分支：git checkout 4b

**2. DataFrame 学习文档：**

[https://pandas.pydata.org/pandas-docs/stable/reference/frame.html](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

# 6. pandas基本操作

**1. 获取课程源码操作方法：**

切换分支：git checkout 4b

**2. Pandas 计算功能操作文档：**

[https://pandas.pydata.org/docs/user_guide/computation.html#method-summary](https://pandas.pydata.org/docs/user_guide/computation.html#method-summary)

# 7. pandas分组聚合

**1. 获取课程源码操作方法：**

切换分支：git checkout 4b

# 8. pandas多表拼接

**1. 获取课程源码操作方法：**

切换分支：git checkout 4b

**2. MySQL 数据库多表连接学习文档：**

[https://dev.mysql.com/doc/refman/8.0/en/join.html](https://dev.mysql.com/doc/refman/8.0/en/join.html)

# 9. pandas输出和绘图

**1. 获取课程源码操作方法：**

切换分支：git checkout 4b

**2. plot 学习文档：**

[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)

**3. seaborn 学习文档：**

[http://seaborn.pydata.org/tutorial.html](http://seaborn.pydata.org/tutorial.html)

# 10. jieba分词与提取关键词

**1. 获取课程源码操作方法：**

切换分支：git checkout 4c

**2. jieba 学习文档：**

[https://github.com/fxsjy/jieba/blob/master/README.md](https://github.com/fxsjy/jieba/blob/master/README.md)

# 11. SnowNLP情感倾向分析

**1. 获取课程源码操作方法：**

切换分支：git checkout 4c

**2. snowNLP 参考学习地址：**

[https://github.com/isnowfy/snownlp/blob/master/README.md](https://github.com/isnowfy/snownlp/blob/master/README.md)

# 本周作业

**作业背景：**在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。

因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

**作业要求：**请将以下的 SQL 语句翻译成 pandas 语句：

```sql
1. SELECT * FROM data;
2. SELECT * FROM data LIMIT 10;
3. SELECT id FROM data; //id 是 data 表的特定一列
4. SELECT COUNT(id) FROM data;
5. SELECT * FROM data WHERE id<1000 AND age>30;
6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
8. SELECT * FROM table1 UNION SELECT * FROM table2;
9. DELETE FROM table1 WHERE id=10;
10. ALTER TABLE table1 DROP COLUMN column_name;
```