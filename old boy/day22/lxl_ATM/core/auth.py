import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)



from conf import settings
from core import db_handler
import time


print(settings.DATABASE)

def acc_auth(account,password):
    '''

    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication,return the account object
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r')as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))#没完
                if time.time()>exp_time_stamp:
                    print("\033[31;1mAccount[%s] has expired,please contact the back to get the new card!\033[0m" %account)#没完
                else: #passed the authentication
                    return account_data
            else:
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(user_data,log_obj):
    '''
    account login func
    :param user_data: user info data,only saves in memory
    :return:
    '''
    retry_count = 0
    while user_data["is_authenticated"] is not True and retry_count < 3:
        account = input("\033[32;1mAccount:\033[0m").strip()
        password = input("\033[32;1mAccount:\033[0m").strip()
        auth = acc_auth(account,password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" %account)
        exit()


