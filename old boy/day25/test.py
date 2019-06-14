import tornado
# def dec():
#     print(123)
#
# foo = type('foo',(object,),{'func':dec})
#
# obj = foo()
# obj.dec


# class Foo:
#     def f1(self):
#         return 111
#     @staticmethod
#     def f2():
#         return 222
#
#     def f3(self):
#         return 333
# obj = Foo()
# # i = input("请输入")
# # v = getattr(obj,i)
# # s = v()
# # print(s)
# print(Foo.f2())


def add():
    print("123")

obj = {"a":add}
obj["a"]()

