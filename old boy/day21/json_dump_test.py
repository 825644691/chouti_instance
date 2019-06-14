import json
# f = open("JSON_DUMP","w")
# dic={'1':'111'}
# json.dump(dic,f)
# f.close()
sss = {"name":"lxl"}
sss = json.dumps(sss)
print(type(sss))
sss =json.loads(sss)
print(type(sss))