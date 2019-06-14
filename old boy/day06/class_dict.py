# a=dict([('name','boy'),])
# print(a)
# a['sex']='boy'
# print(a)


#增
# ret = a.setdefault('sex','girl')#setdefault有返回值
# print(ret)
# print(a)
# ret1 = a.setdefault('hobby','girl')
# print(ret1)
# print(a)

#查
# dic3 = {'age':'21','name':'Lacey','hobby':'girl'}
# print(dic3['age'])
# print(dic3.keys())
# print(list(dic3.values()))
# print(type(dic3.items()))


#改

# print(dic4)


#删
# ret = dic4.pop('hobby')#pop函数有返回值
# print(ret)
# print(dic4)
# del dic4['name']#删除字典的特指的一个键值对，没有返回值
# del dic4#删除整个字典
# dic4.popitem()#随机删除该字典的随机键值对
# dic4.clear()#清空字典


#其他操作涉及的方法
#1
# dic6 = dict.fromkeys(['host1','host2','host3'],['test1','test2'])
# print(dic6)
# dic6['host2'][1] = 'abc'
# print(dic6)

#2
# dic = {5:'555',4:'444',2:'222'}
# print(sorted(dic))#键排序,只输出键
# print(sorted(dic.values()))#值排序，只输出值
# print(sorted(dic.items()))#键排序，输出键和值

#3遍历
dic = {'name':'Lacey','age':'21'}
# for i in dic.items():
#     #默认打印键
#     print(i)

for i in dic:
    print(i,dic[i])