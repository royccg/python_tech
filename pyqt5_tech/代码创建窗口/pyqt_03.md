<!-- TOC -->

- [第3部分学习](#%E7%AC%AC3%E9%83%A8%E5%88%86%E5%AD%A6%E4%B9%A0)
    - [对话框：QDiaglog](#%E5%AF%B9%E8%AF%9D%E6%A1%86qdiaglog)

<!-- /TOC -->

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

# 数据
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
