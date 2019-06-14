#深拷贝即是两份独立的内存空间

#浅拷贝
#1不影响
# s = [1,'lxl','liangxiaoli']
# d = s.copy()
# d[1] = 'lgl'
# print(s)
# print(d)

#2影响
s = [[1,2,3],'lxl','liangxiaoli']
d = s.copy()
d[0][0] = 2
d[2] = 'lxllxl'
print(s)
print(d)

#深拷贝
# import copy
#
#
# s = [[1,2,3],'lxl','liangxiaoli']
# d = copy.deepcopy(s)
# d[0][1] = 3
# print(s)
# print(d)