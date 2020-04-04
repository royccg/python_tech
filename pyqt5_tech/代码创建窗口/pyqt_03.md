
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [第3部分学习](#第3部分学习)
    - [对话框：QDiaglog](#对话框qdiaglog)
  - [Draw](#draw)
    - [绘图API：绘制文本](#绘图api绘制文本)
    - [用像素点绘制正弦曲线](#用像素点绘制正弦曲线)
    - [绘制不同类型的直线](#绘制不同类型的直线)
    - [绘制各种图形](#绘制各种图形)
    - [用画刷填充图形区域](#用画刷填充图形区域)
  - [其余操作](#其余操作)
    - [让控件支持拖拽](#让控件支持拖拽)
    - [使用剪贴板](#使用剪贴板)
    - [日历控件](#日历控件)
    - [输入各种风格的日期和时间](#输入各种风格的日期和时间)
    - [创建和使用菜单](#创建和使用菜单)
    - [创建和使用状态栏](#创建和使用状态栏)
    - [使用打印机](#使用打印机)
- [数据 table控件](#数据-table控件)
    - [显示二维表数据](#显示二维表数据)
    - [在单元格中放置控件](#在单元格中放置控件)
    - [在表格中搜索Cell和行定位](#在表格中搜索cell和行定位)
    - [设置单元格字体和颜色](#设置单元格字体和颜色)
    - [按表格中的某一列排序](#按表格中的某一列排序)
    - [设置单元格文本的对齐方式](#设置单元格文本的对齐方式)
    - [合并单元格](#合并单元格)
    - [设置单元格的尺寸](#设置单元格的尺寸)
    - [实现单元格中图文混排](#实现单元格中图文混排)
    - [改变单元格中图片的尺寸](#改变单元格中图片的尺寸)
    - [在表格中显示上下文菜单](#在表格中显示上下文菜单)
    - [树控件（QTreeWidget）的基本用法](#树控件qtreewidget的基本用法)
    - [QTreeView控件与系统定制模式](#qtreeview控件与系统定制模式)
- [容器控件](#容器控件)
    - [选项卡控件QTabWidget](#选项卡控件qtabwidget)
    - [堆栈窗口控件（QStackedWidget）](#堆栈窗口控件qstackedwidget)
    - [停靠控件（QDockWidget）](#停靠控件qdockwidget)
    - [容纳多文档的窗口](#容纳多文档的窗口)
    - [滚动条控件](#滚动条控件)
- [Multithread 多线程完成任务](#multithread-多线程完成任务)
    - [动态显示当前时间](#动态显示当前时间)
    - [让程序定时关闭](#让程序定时关闭)
    - [使用线程类（QThread）编写计数器](#使用线程类qthread编写计数器)
- [web 浏览器控件](#web-浏览器控件)
    - [用Web浏览器控件（QWebEngineView）显示网页](#用web浏览器控件qwebengineview显示网页)
    - [显示嵌入页面](#显示嵌入页面)
    - [PyQt5调用JavaScript代码](#pyqt5调用javascript代码)
    - [JavaScript调用Python函数计算阶乘](#javascript调用python函数计算阶乘)
- [布局](#布局)
  - [水平盒布局（QHBoxLayout）](#水平盒布局qhboxlayout)
    - [设置控件的对齐方式](#设置控件的对齐方式)
  - [垂直盒布局](#垂直盒布局)
  - [](#)

<!-- /code_chunk_output -->

# 第3部分学习
### 对话框：QDiaglog
+ QMessageBox
  - 关于对话框
  - 错误对话框
  - 警告对话框
  - 提问对话框
  - 提问对话框
  - 消息对话框
  ```text
  有两点不一致
   1.显示的对话框图标可能不同
   2.显示的按钮是不一样的
  ```
+ QColorDialog
  - 文字颜色 和背景色
+ QFileDialog
  - 打开文件和保存文件对话框
+ QFontDialog
  - 设置 字体
+ QInputDialog
  - 输入对话框
  - QInputDialog.getItem 显示输入列表、元组
  - QInputDialog.getText 录入文本
  - QInputDialog.getInt 计数器控件

## Draw
### 绘图API：绘制文本

+ 文本
+ 各种图形（直线、点、椭圆、弧、扇形、多边形等）
+ 图像

** 必须在paintEvent事件方法中绘制各种元素**
```text
QPainter

painter = QPainter()
painter.begin()
painter.drawText(....)
painter.end()

```

### 用像素点绘制正弦曲线
+ 采用drawPoint(x,y)

### 绘制不同类型的直线
+ 虚线  或者  点划线
+ 通过钢笔（Pen） 的样式来实现

### 绘制各种图形
+ 弧
+ 圆形
+ 椭圆
+ 矩形
+ 多边形
+ 绘制图像

### 用画刷填充图形区域
+ QBrush

## 其余操作
### 让控件支持拖拽
+ setAcceptDrops(True)
+ setDragEnabled(True)
+ 接收的控件 需要两个事件
  - dragEnterEvent  被拖拽控件 移至  接收区域时触发
  - dropEvent    在接收区域内 放下 被拖拽控件时 触发

### 使用剪贴板
通过代码将文本复制到剪贴板，然后复制到 程序内

### 日历控件
允许用户选择日期
+ QCalendarWidget

### 输入各种风格的日期和时间
+ 显示时间
+ 事件

### 创建和使用菜单
+ 工具栏
  - 工具栏默认按钮：只显示图标，将文本作为悬停提示
  - 三种显示状态
    - 只显示图标
    - 只显示文本
    - 显示图标和文本

### 创建和使用状态栏

### 使用打印机
+ 输入都是以图像的形式输出

# 数据 table控件
### 显示二维表数据
+ QTableView控件
  - 数据源：Model
  - 需要创建QTableView实例和一个数据源（Model），然后将两者关联
  - MVC ：Model Viewer Controller
    - MVC的目的是将后端的数据和前端的页面的耦合度降低
+ QTableWidget
  - QTableView的扩展
  - 每一个Cell（单元格）shi yige QTableWidgetItem

+ QListView控件
  - 数据源Model
+ QListWidget
  - QListView 支持非MVC模式

### 在单元格中放置控件
+ setCellWidget 将控件放到单元格中
+ setItem 将文本放入单元格中
+ QSS QtStyleSheet
  - setStyleSheet:设置控件样式

### 在表格中搜索Cell和行定位
+ 数据的定位： findItems
+ 如果找到满足条件的单元格，会定位到单元格所在的行
  - setSliderPosition(row)

### 设置单元格字体和颜色
+ 字体名称
+ 字号
+ 颜色

### 按表格中的某一列排序
+ 按哪一列排序
+ 排序类型：升序或降序
+ sortItems(columnIndex, orderType)

### 设置单元格文本的对齐方式
+ setTextAlignment
  - Qt.AlignRight
  - Qt.AlignBottom

### 合并单元格
+ setSpan(row, col, 要合并的行数，要合并的列数)

### 设置单元格的尺寸
+ setRowHeight(0, 100)
+ setColumnWidth(0, 150)

### 实现单元格中图文混排

```python
newItem = QTableWidgetItem(QIcon('new.png'), '打开')
```

### 改变单元格中图片的尺寸
+ setIconSize(QSize(width, height))

### 在表格中显示上下文菜单
+ 表格中 单击右键能出现菜单
+ QMenu.exec_
1. 如何弹出菜单
2. 如何在满足条件的情况下弹出菜单
   1. 判断条件
   2. 不满足就不成立

```python
# 允许使用上下文菜单
self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
```

### 树控件（QTreeWidget）的基本用法
+ 添加响应事件
+ 添加、修改和删除树控件中的节点

### QTreeView控件与系统定制模式
+ 使用model装载控件
    + QDirModel

# 容器控件
### 选项卡控件QTabWidget
+ 多个页面

### 堆栈窗口控件（QStackedWidget）
+ 多注意

### 停靠控件（QDockWidget）
可停靠到 上下左右的  区域的控件

### 容纳多文档的窗口
+ QMdiArea
+ QMdiSubWindow

### 滚动条控件
+ QScrollBar
    + 通过滚动条值得变化控制其他控件状态的变化
    + 通过滚动条值得变化控制控件的变化

# Multithread 多线程完成任务
### 动态显示当前时间
+ QTimer
+ QThread
+ 多线程：用于同时完成多个任务
+ 每隔一定时间  调动函数

### 让程序定时关闭
+ QTimer.singleShot


### 使用线程类（QThread）编写计数器
+ QThread

```python
def run(self):
    while True:
        self.sleep(1)
        if sec ==5:
            break
```

+ QLCDNumber
+ 用到自定义信号

# web 浏览器控件
### 用Web浏览器控件（QWebEngineView）显示网页
+ PyQt5 和Web的交互技术
    + 同时使用Python 和Web开发程序，混合开发
    + Python+JavaScript+HTML5+CSS
+ QWebEngineView

### 显示嵌入页面

### PyQt5调用JavaScript代码
+ PyQt5和JavaScript交互
+ 交互
    + PyQt5 <-> JavaScript互相传递数据

### JavaScript调用Python函数计算阶乘
+  将Python的一个对象映射到JavaScript中
+  将槽函数映射到JavaScript中


# 布局
## 水平盒布局（QHBoxLayout）
### 设置控件的对齐方式
+ 左对齐
+ 右对齐
+ 上下对齐

## 垂直盒布局

## 设置布局的伸缩量（addStretch）
+ 默认右对齐
+ 伸缩量为0的 先排，其余的控件再排

## 让按钮永远在窗口的右下角
