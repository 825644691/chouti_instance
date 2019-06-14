#单例模式，只用一个实例（对象）

# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print('%s-%s' %(self.name,self.age))


#obj = Foo('lxl',18) #obj就是一个实例
#第一个方法（不常用）
# v = None
# while True:
#     if v:
#         v.show()
#     else:
#         v = Foo('lxl',18)
#         v.show()


class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

#用单例模式不在使用单例模式来创建对象
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
obj3 = Foo.get_instance()
print(obj3)




# class Fooo:
#     @classmethod
#     def get_instance(cls):
#         if not hasattr(Fooo,'_v'):
#             if not hasattr(Fooo,'_v'):
#                 cls._v = Fooo()
#         return cls._v
#
# obj1 = Fooo.get_instance()
# print(obj1)
# obj2 = Fooo.get_instance()
# print(obj2)
# obj3 = Fooo.get_instance()
# print(obj3)
