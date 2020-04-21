
class Person():

    country = '中国'
    # 声明类属性，并且赋值
    # 实例属性通过构造方法来声明
    #  self 不是关键字，代表的是当前对象

    def __init__(self, name, age, food):
        print('构造方法被调用')
        # 构造函数，初始化属性
        self.name = name   # 通过self 创建实例属性，并且赋值
        self.age = age
        self.food = food

    # 创造普通方法
    def Eat(self):
        print('%s 今年 %s， 喜欢吃%s，我来自%s' % (self.name, self.age, self.food, Person.country))
        #  对象属性用self调用， 类属性用 类名 调用 （Person）


xiaoming = Person("小明", 16, "巧克力")

# 通过对象调用实例方法
xiaoming.Eat()
setattr(xiaoming, "name", "xziao")
print(xiaoming.name)
