import shelve

f = shelve.open('shelve')
f['info'] = {'name':'lxl','age':'19'}
data = f.get('info')
print(data['name'])
f.close()