

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
 +
