<!-- TOC -->

- [pyqt5的基础知识](#pyqt5%E7%9A%84%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86)
    - [什么是Qt](#%E4%BB%80%E4%B9%88%E6%98%AFqt)
    - [什么是pyQt](#%E4%BB%80%E4%B9%88%E6%98%AFpyqt)
    - [讲解的内容](#%E8%AE%B2%E8%A7%A3%E7%9A%84%E5%86%85%E5%AE%B9)
- [搭建PyQt5开发环境](#%E6%90%AD%E5%BB%BApyqt5%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83)
- [开发第一个基于PyQt5的桌面应用](#%E5%BC%80%E5%8F%91%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%9F%BA%E4%BA%8Epyqt5%E7%9A%84%E6%A1%8C%E9%9D%A2%E5%BA%94%E7%94%A8)
- [安装和配置QtDesigner](#%E5%AE%89%E8%A3%85%E5%92%8C%E9%85%8D%E7%BD%AEqtdesigner)
- [将.ui文件生成.py文件](#%E5%B0%86ui%E6%96%87%E4%BB%B6%E7%94%9F%E6%88%90py%E6%96%87%E4%BB%B6)
- [在QtDesigner中使用水平、垂直、网格、表单布局](#%E5%9C%A8qtdesigner%E4%B8%AD%E4%BD%BF%E7%94%A8%E6%B0%B4%E5%B9%B3%E5%9E%82%E7%9B%B4%E7%BD%91%E6%A0%BC%E8%A1%A8%E5%8D%95%E5%B8%83%E5%B1%80)
- [尺寸策略（sizepolicy）](#%E5%B0%BA%E5%AF%B8%E7%AD%96%E7%95%A5sizepolicy)
    - [sizeHint(期望尺寸)](#sizehint%E6%9C%9F%E6%9C%9B%E5%B0%BA%E5%AF%B8)
    - [尺寸设置](#%E5%B0%BA%E5%AF%B8%E8%AE%BE%E7%BD%AE)

<!-- /TOC -->

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

# 安装和配置QtDesigner
使用pycharm来整合 QtDesigner

# 将.ui文件生成.py文件
+ python -m PyQt5.uic.pyuic demo.ui -o demo.py
+ pyuic5 demo.ui -o demo.py

# 在QtDesigner中使用水平、垂直、网格、表单布局
构件在布局中是等分、等距的

#  尺寸策略（sizepolicy）
### sizeHint(期望尺寸)
 + 在未设置控件的最大最小值时的，建议尺寸（默认尺寸）
 + 对于大多数控件来说，sizeHint的值是可读的
 + 读取期望尺寸
    ```python
    self.pushButton.sizeHint().width()
    self.pushButton.sizeHint().height()
    ```
  + 最小期望尺寸（minimumSizeHint）
    + 很多控件的 期望和最小期望尺寸是相同的

  ```python
  self.pushButton.minimunSizeHint().width()
  self.pushButton.minimunSizeHint().height()
  ```

### 尺寸设置

# 设置控件之间的伙伴关系
edit-setbuddied

# 修改控件的Tab顺序
