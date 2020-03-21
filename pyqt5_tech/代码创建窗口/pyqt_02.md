
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
