import logging
import os


LOG_LEVEL = logging.WARNING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#上两级目录

LOG_TYPES = {
    'transaction':'transactions.log',
    'access':'access.log',

}

DATABASE={
    'engine':'file_storage',#support mysql in the future
    'name':'accounts',
    'path':'%s/db' % BASE_DIR
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05},
    'consume':{'action':'minus','interest':0}
}

