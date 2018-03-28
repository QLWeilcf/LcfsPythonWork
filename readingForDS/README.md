从今天（2018-3-13）到3月26号本目录下会更新《Python数据分析基础》这本书的一些读书笔记和思考。
## 书目信息：

原书名: Foundations for Analysis with Python
中文翻译版: Python数据分析基础
原作：Clinton W. Brownley
人民邮电出版社出版，2017年8月第一版。

![image](./dsIpynbPic/foundationsForAnalyWithPyBookCover.png)

本书关于基础知识的内容很多，作者也说：
> 本书面向的读者是那些经常使用电子表格软件进行数据处理，但从未写过一行代码的人。
因此对于数据的读入讲得比较多，重点讲了csv、Excel、SQL的读取与处理。关于一些建模和挖掘的算法讲得比较少。阅读完本书后会补充一些算法的内容（特别是关联分析和聚类的算法）。

### plan

- [x] Day 1 [第1章 Python基础_数据表示](./chpOnePyFoundation.ipynb)   #3.13
- [x] Day 2 [第1章 Python基础_数据结构与文件读写](https://github.com/QLWeilcf/cunyu/blob/master/chpOneDataContainer.ipynb)   #3.14
- [x] Day 3 [第2章 CSV文件](./chpTwoRWcsvData.ipynb)   #3.15
- [x] Day 4 [第3章 Excel文件](./chpThreeRWExcel.ipynb)   #3.16
- [x] Day 5 [第4章 数据库_sqlite3学习与深入](./chpFourDBsqlite.ipynb)   #3.17
- [x] Day 6 [第4章 数据库_MySQL](./chpFourdbMySQL.ipynb)  #3.18
- [x] Day 7 [第5章 应用程序](./chpFiveSmallApplct.ipynb)  #3.19
- [x] Day 8 [第6章 图与图表_matplotlib](./chpSixChartsPlot.ipynb)  #3.20
- [x] Day 9 [第6章 图与图表_其他可视化库](./chpSixChartsVis.ipynb)   #3.21
- [x] Day 10 [第7章 描述性统计建模](./chpSevenDescStat.ipynb)   #3.22
- [x] Day 11 [第8章 按计划自动运行脚本](./chpEightAutoScripts.ipynb)   #3.23
- [x] Day 12 [第9章 从这里启航_更多模块和数据结构](./chpNineSetSail.ipynb)   #3.24
- [x] Day 13 [关联分析_Apriori](./chpTenCorAnlyApriori.ipynb)  #3.25
- [x] Day 14 [关联分析_FP Tree](./chpTenCorAnlyFPTree.ipynb)  #3.26

#### 简书版

- [x] Day 1 [第1章 Python基础_数据表示](https://www.jianshu.com/p/00f763de8752)
- [x] Day 2 [第1章 Python基础_数据结构与文件读写](https://www.jianshu.com/p/d357d0e87a41)
- [x] Day 3 [第2章 CSV文件](https://www.jianshu.com/p/78f13ad85859)
- [x] Day 4 [第3章 Excel文件](https://www.jianshu.com/p/49f30e298d99)
- [x] Day 5 [第4章 数据库_sqlite3学习与深入](https://www.jianshu.com/p/57f36c5a4b3a)
- [x] Day 6 [第4章 数据库_MySQL](https://www.jianshu.com/p/6d45437eba3c)  
- [x] Day 7 [第5章 应用程序](https://www.jianshu.com/p/825a658cd263)
- [x] Day 8 [第6章 图与图表_matplotlib](https://www.jianshu.com/p/cd3a13e0d302)
- [x] Day 9 [第6章 图与图表_其他可视化库](https://www.jianshu.com/p/d7ad5434f5a2)
- [x] Day 10 [第7章 描述性统计建模](https://www.jianshu.com/p/73d81407587c)
- [x] Day 11 [第8章 按计划自动运行脚本](https://www.jianshu.com/p/ea5cd671b662)
- [x] Day 12 [第9章 从这里启航_更多模块和数据结构](https://www.jianshu.com/p/28856f16d428)
- [x] Day 13 [关联分析_Apriori](https://www.jianshu.com/p/5cc6b3f34afc)
- [x] Day 14 [关联分析_FP Tree](https://www.jianshu.com/p/a3c97d868a5b)

### 笔记中涉及到的数据
- [supplier_data.csv](./supplier_data.csv) 第2章 CSV文件读写 用到的数据
- [sales_2015.xlsx](./sales_2015.xlsx)  第3章 Excel文件读写 用到的数据
- [mysql_server_error_log.txt](https://github.com/cbrownley/foundations-for-analytics-with-python/blob/master/applications/mysql_server_error_log.txt) 第5章 应用程序 用到的数据


---
### 书摘

> 一旦你意识到可以高效地完成那些枯燥无味、浪费时间、容易出错的手工不可能完成的任务，就会感到一种激情流遍全身，迫不及待地希望使用 Python 去完成更多的问题和任务。这就是我希望你去做的事情，从这里启航，选择一个重要的问题或任务去攻克，直到你的代码正确运行，到达胜利的彼岸。
