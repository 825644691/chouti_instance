'''
定义
   函数：
       def + 函数名（参数）
   面向对象:
       class => 类
       def =>方法
       ##### self

执行:
    函数：
        函数名(参数)
    面向对象： =>创建一个对象(中间人)来接收类
    o = bar() #创建中间人(对象)来接收bar()这个类
    o.say()
'''

# class Father:
#     def say(self):
#         print( self.name, self.sex)
#
#
#
# class bar(Father):
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#
#
#     def say(self):
#         Father.say(self)
#         #super(bar,self).say()
#         return 1
#
#
#
# what = "尼玛的"
# say = bar('lxl','boy')
#
# o = say.say()
# print(o)

# sat = bar()
# sat.name = "lxlxl"
# sat.say(what)

# def say1(what):
#     print(what)
#
# say1(what)

class person:
    # def __init__(self,name,sex,fight,age):
    #     self.name = name
    #     self.sex = sex
    #     self.fight = fight
    #     self.age = age

    def pla(self):
        #普通方法
        pass

    @staticmethod
    def place():
        #静态方法，类直接调用
        pass


    @classmethod
    def fht(self):
        pass
    #类对象，cls是类名，由类直接调用


    @property
    def fig(self):
        #执行 用self.fig
        #属性或者特性
        return 0

    @fig.setter #self.fig = 123 自动调用
    def fig(self,val):
        print(val)
    @fig.deleter #del fig.deleter 自动调用
    def fig(self):
        print(666)



# y_n = input("是否创建角色 y or n")
# if y_n == 'y':
#     name = input("请输入角色名字")
#     sex = input("请输入角色性别")
#     fight = input("请输入")
#     age = input("请输入年龄")


# obj = person()
# s = obj.fig
# print(s)
# obj.fig = 1
# del obj.fig


class FOO:
    def __init__(self,name,age):
        self.name =name
        self.__age = age #私有，外部不能直接访问

    def show(self):
        print(self.__age)


    def f1(self):
        return 123

    def f2(self,val):
        print(val)

    def f3(self):
        print("del")

    per = property(fget=f1,fset=f2,fdel=f3)


#类成员属性的第二种写法
# obj = FOO()
# ret = obj.per
# print(ret)
# obj.per = 3
# print(obj.per)
#
# del obj.per


#私有成员的间接访问
# obj = FOO('LXL',16)
# obj.show()


class FOOO:

    __v = "123"#静态字段的私有化
    def __init__(self):
        pass

    @staticmethod
    def show():
        print(FOOO.__v)


    def show1(self):
        print(self.__v)


    def __f1(self):
        print(123)


    def f2(self):
        self.__f1()
        #私有方法的访问方法

    def f3(self):
        show1()


#
# FOOO.show()
# FOOO().f2()

FOOO().f2()


'''
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def __str__(self):
        return '%s-%s' %(self.name,self.age)

    def show(self):
        print('%s-%s' %(self.name,self.age))
        


obj = Foo('lxl',18)

print(obj)#print一个对象自动执行函数的__str__方法
obj.show()
'''

'''
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __add__(self, other):
        #加减乘除方法都一样
        return 'lxlxllxl'

    def __del__(self):
        print('析构方法，对象被销毁时自动执行')

    def __getitem__(self, item):
        return item


obj1 = Foo('lxl',18)
obj2 = Foo('xjw',18)
r = obj1 + obj2
#两个对象相加时，自动执行第一个对象的__add__方法，并且
#将第二个对象当作参数传到__add__方法的other中
print(r,type(r))
obj = Foo('lxl',19)
print(obj.__dict__)#obj中的字段以字典的形式返回
print(Foo.__dict__)#把类的方法全部显示出来
print(obj[1])
r = obj[1]#自动执行li对象类中的__getitem__方法，8作为参数传给item
'''