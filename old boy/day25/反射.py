#反射(用字符串操作类中的属性)
#getattr(对象,属性)获取对象中属性(对象，方法等等)的值，属性是一个字符串,当属性是一个字符串或者用INPUT输入的值的时候
#hasattr(对象，属性)检测对象中是否含有某个属性，其中属性是一个字符串
#setattr(对象，属性，值)，给对象设置属性和值
#delattr(对象，属性)，删除对象中的某个属性，属性是一个字符串

class Foo:
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def show(self):
        return '%s-%s' %(self.name,self.age)

obj = Foo('lxl',18)
b = 'name'
srr = getattr(obj,b)
print(srr)
func = getattr(obj,'show')
r = func()
print(r)
print(hasattr(obj,'show'))
setattr(obj,'v1','v2')
print(obj.v1)
delattr(obj,'show')
print(obj.show())

