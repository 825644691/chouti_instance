'''
while True:
    try:
        imp = input("请输入序号")
        imp = int(imp)
    except KeyError as e:
        print('KeyError',e)
    except ValueError as e:
        print('ValueError',e)
    except Exception as e:
        #e时Exception的对象
        imp =1
        print(e)
    else:
        print("try中无错误执行else")
    finally:
        print("无论try中代码正不正确都执行finally")
        print(imp)
'''

'''
def db():
    pass

def index():
    try:
        db()
        raise Exception('数据库错误')
    except Exception as e:
        str_error = str(e)
        print(str_error)
        #记录错误：打开文件写日志

index()
'''

#自定义异常：
class LxlError(Exception):
    def __init__(self,masg):
        self.message = masg

    def __str__(self):
        return self.message

try:
    raise LxlError("我错了")
except LxlError as e:
    print(e)

