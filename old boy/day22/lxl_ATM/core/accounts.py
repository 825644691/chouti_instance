from core import db_handler
from  conf import settings
import json



def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account_id)
    with open(account_file) as f:
        acc_data = json.load(f)
        return acc_data

def dump_account(account_data):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_data['id'])
    with open(account_file,'w') as f:
        acc_data = json.dump(account_data,f)
    return True