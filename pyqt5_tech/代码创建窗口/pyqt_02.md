
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [开始使用代码来 设计PyQt5](#开始使用代码来-设计pyqt5)
  - [主窗口类型](#主窗口类型)
  - [让主窗口居中](#让主窗口居中)
  - [退出应用程序](#退出应用程序)
  - [屏幕坐标系](#屏幕坐标系)
  - [设置窗口和应用程序图表](#设置窗口和应用程序图表)
  - [为控件添加提示消息](#为控件添加提示消息)
  - [QLabel控件的基本用法](#qlabel控件的基本用法)
  - [QLabel 与伙伴控件](#qlabel-与伙伴控件)
  - [QLindeEdit 控件与回显模式](#qlindeedit-控件与回显模式)
  - [QLineEdit控件的输入（校验器）](#qlineedit控件的输入校验器)
  - [用掩码限制QLineEdit控件的输入](#用掩码限制qlineedit控件的输入)
  - [QLineEdit综合案例](#qlineedit综合案例)
  - [QTextEdit控件输入多行文本](#qtextedit控件输入多行文本)
  - [按钮控件（QPushButton）](#按钮控件qpushbutton)

<!-- /code_chunk_output -->


# 开始使用代码来 设计PyQt5
## 主窗口类型

 + 有3种窗口
   - QMainWindow
     - 可以包含菜单栏、工具栏、状态栏和标题栏
     - 是最常见的窗口形式
   - QWidget
     - 不确定窗口的用途
     - 可以代替主窗口和对话框
   - QDialog
     - 对话窗口的基类
     - 主要是执行短期任务
     - 没有菜单栏、工具栏和状态栏的

## 让主窗口居中
 运行程序时，窗口在屏幕的居中位置
 + 进行手工的计算距离
   - 经过类 QDesktopWidget来计算
 ```python
 def center(self):
     # 获取屏幕坐标系
     screen = QDesktopWidget().screenGeometry()
     # 获取窗口坐标系
     size = self.geometry()
     newLeft = (screen.width() - size.width())/2
     newTop = (screen.height() - size.height())/2
     self.move(newLeft, newTop)
 ```

## 退出应用程序

 + 通过手工代码，来创建button来退出应用程序

## 屏幕坐标系

 + 屏幕内的坐标系
 + 左上角的坐标为（0,0）


## 设置窗口和应用程序图表

 + 在窗口的实例化中 使用 app.setWindowTitle(QIcon(""))的方式
     + pc和mac上 都有图表
 + 使用 窗口的设置代码中加入 setWindowTitle(QIcon(""))的
     + pc上有，mac的标题栏上没有 图标

    ```Text
        IconForm.py
    ```

## 为控件添加提示消息

 ```Text
 ToolTip.py
 ```

## QLabel控件的基本用法

 + setAlignment()  设置文本的对齐方式
 + setIndent() 设置文本缩进
 + text()  获取文本内容
 + setBuddy() 设置伙伴关系
 + setText() 设置文本内容
 + selectedText() 返回所选择的字符
 + setWordWrap() 设置是否允许换行

 + Qlabel常用的信号（事件）：
     + 当鼠标滑过QLabel 控件时触发： lineHovered
     + 当鼠标单击QLabel 控件时触发： lineActivated

## QLabel 与伙伴控件

```Text
QLabelBuddy.py
```

## QLindeEdit 控件与回显模式
 + 基本功能：输入单行的文本
 + EchoMode （回显模式），4种
     + Normal,正常 ，全部显示
     + NoEcho，不显示
     + Password 用特殊字符代替
     + PasswordEchoOnEdit  半代替


## QLineEdit控件的输入（校验器）
 + 如限制只能输入整数、浮点数或满足一定条件的字符串


## 用掩码限制QLineEdit控件的输入

    A  ASCII字母字符是必须输入的（A-Z、a-z）
    a  ASCII字母字符是允许输入的，但不是必需的 （A-Z、a-z）
    N  ASCII字母字符是必须输入的（A-Z、a-z、0-9）
    n  ASCII字母字符是允许输入的，但不是必需的 （A-Z、a-z、0-9）
    X  任何字符都是必须输入的
    x  任何字符都是允许输入的，但不是必需的
    9  ASCII数字字符是必须输入的（0-9）
    0  ASCII数字字符是允许输入的，但不是必需的（0-9）
    D  ASCII数字字符是必须输入的（1-9）
    d  ASCII数字字符是允许输入的，但不是必需的（1-9）
    #  ASCII数字字符或加减符号是允许输入的，但不是必需的
    H  十六进制格式字符是必须输入的（A-F、a-f、0-9）
    h  十六进制是允许输入的，但不是必需的（A-F、a-f、0-9）
    B  二进制格式字符是必须输入的（0，1）
    b  二进制格式字符是允许输入的，但不是必需的（0，1）
    >  所有的字母字符都大写
    <  所有的字母字符都小写
    !  关闭大小写转换
    \  使用"\"转义上面列出的字符

## QLineEdit综合案例

```Text
QLineEditDemo.py
```

## QTextEdit控件输入多行文本
可以多行输入


## 按钮控件
+ QAbstractButoon
    + QPushButton
    + AToolButton
    + QRadioButton（单选框控件）
    + QCheckBox(复选框控件)
        + 3种状态
        + 未选中： 0
        + 半选中： 1
        + 选中：  2

## 下拉列表控件
+ 如何将列表项添加到QComboBox控件中
+ 如何获取选中的列表项

## 计数器控件（QSpinBox）
