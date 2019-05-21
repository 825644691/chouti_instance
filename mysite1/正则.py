import re


ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})', 'weeew34ttt123/ooo')
print(ret.group())
print(ret.group('id'))
