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
