import subprocess


#subprocess.Popen()会自己创建一个子进程,第一个参数必须是一个字符串
# a = subprocess.Popen('dir',shell=True)
# print(a)
# a = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE)
# s = str(a.stdout.read(),'gbk')
# print(s)
# stdout = subprocess.PIPE 把输出结果传输到主进程中，封装在a对象中
#如果不写，直接在子进程中输出

data = 0
if len(data) !=1024:
