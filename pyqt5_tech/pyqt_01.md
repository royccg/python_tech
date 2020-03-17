<!-- MarkdownTOC -->

- pyqt5的基础知识
    - 什么是Qt
    - 什么是pyQt
    - 讲解的内容
- 搭建PyQt5开发环境
- 开发第一个基于PyQt5的桌面应用

<!-- /MarkdownTOC -->
# pyqt5的基础知识
## 什么是Qt
使用C++语言编写的跨平台GUI库，支持Window、MacOSx和linux。由于Qt使用C++语言编写，所以使用Qt开发的GUI程序的风格与当前操作系统完全相同，而且运行效率很高。

## 什么是pyQt
pyQt是一个用于创建GUI应用程序的跨平台的跨平台工具包，它将Python与Qt库融为一体。也就是说，PyQt允许使用Python语言调用Qt库中的API。这样做的最大好处就是在保留了Qt高运行效率的同时，大大提高了开发效率。因为，使用Python语言开发程序要比使用C++语言开发程序快很多。PyQt对于Qt做了完整的封装，几乎可以用PyQt做Qt能做的任何事情。

## 讲解的内容
 + Qt Designer
 + PyQt5基本窗口控件（QMainWindow、Qwidget、Qlabel、QLinEdit、菜单、工具栏等）
 + PyQt5高级组件（QTableView、QListView、容器、多线程等）
 + PyQt5布局管理（QBoxLayout、QGridLayout、QFormLayout、嵌套布局等）
 + PyQt5信号与槽（事件处理、数据传递等）
 + PyQt5图形与特效（定制窗口风格、绘图、QSS与UI美化、不规则窗口、设置样式等）
 + PyQt5扩展应用（制作PyQt5安装程序、数据处理、第三方绘图库在PyQt5中的应用、UI自动化测试等）

# 搭建PyQt5开发环境
 + Python
   - Anacoda
   - python
 + PyQt5模块
 + Pycharm

# 开发第一个基于PyQt5的桌面应用
必须使用两个类 ：QApplication和QWiget。都在PyQt5.QtWidgets。