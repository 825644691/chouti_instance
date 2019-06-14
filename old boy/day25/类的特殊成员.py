
#对象加括号自动执行__call__方法
#类后面加括号自动执行__init__方法
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("call")

    def __int__(self):
        return 123

    def __str__(self):
        return 'lxl'



obj = Foo()
obj()
Foo()()#对象
i = int(obj)#把对象转换成int类型，函数要有__int__方法
print(i,type(i))
s = str(obj)#把对象转换成str类型，函数要有__str__方法
print(s,type(s))

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


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        # 加减乘除方法都一样
        return 'lxlxllxl'

    def __del__(self):
        print('析构方法，对象被销毁时自动执行')

    def __getitem__(self, item):
        if type(item) ==slice:
            return '%s-%s-%s' %(item.start,item.stop,item.step)
        else:
            print('用户希望索引取值')


    def __setitem__(self, key, value):
        print("%s-%s" %(key,value))

    def __delitem__(self, key):
        print(key)

    def __iter__(self):
        return iter([11,22,33])


obj1 = Foo('lxl', 18)
obj2 = Foo('xjw', 18)
r = obj1 + obj2
#如果类中有__iter__方法，对象=》可迭代对象
#对象.__iter__的返回值：迭代器、
#for循环，迭代器，next取下一个值
#for循环，可迭代对象，对象.__iter__()拿到迭代器，再用next取
# 两个对象相加时，自动执行第一个对象的__add__方法，并且
# 将第二个对象当作参数传到__add__方法的other中
print(r, type(r))
# obj = Foo('lxl', 19)
print(obj.__dict__)  # obj中的字段以字典的形式返回
print(Foo.__dict__['__init__'])  # 把类的方法全部显示出来
# print(obj[1])
# r = obj[1]  # 自动执行obj对象类中的__getitem__方法，8作为参数传给item
# obj[10] =123 #自动执行obj对象类中的__setitem__方法，10和123
#              #分别作为key，value的参数
# print(obj[1:3:2])
# li = Foo()
# #1。执行li对象的中类的__iter__方法，并获取其返回值
# #循环上一部中返回的对象
# for i in li:
#     print(i)
