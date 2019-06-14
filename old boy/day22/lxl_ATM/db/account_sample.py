import json
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
print(sys.path)



acc_dic = {
    'id':1234,
    'password':'abc',
    'credit':15000,
    'balance':15000,
    'enroll_date':'2016-01-02',
    'expire_date':'2021-01-01',
    'pay_day':22,
    'status':0 #0 = normal,1 = locked, 2 = disabled
}

print(json.dumps(acc_dic))
