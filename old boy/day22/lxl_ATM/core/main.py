import os
import sys


from core import logger,auth,transaction,accounts

#transaction logger
trans_logger = logger.logger('transaction')
#transaction logger
access_logger = logger.logger('access')


user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def account_info(acc_data):
    print(user_data)

def transfer(acc_data):
    pass

def pay_back(acc_data):
    pass

def logout(acc_data):
    pass


def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :param acc_data: accounts.load_current_balance(acc_data['account_id'])
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    #for k,v in account_data.items():
    #print(k,v)
    current_balance = '''------------balance info--------------
        Credit:    %s
        Balance:   %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) >0 and repay_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' %repay_amount)

def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''------------balance info--------------
            Credit:    %s
            Balance:   %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' %withdraw_amount)

def interactive(acc_data):
    '''

    interact with user
    :return:
    '''
    menu = u'''
    -----------lxl Bank-----------
    \033[32;1m1.  账号信息
    2. 还款(功能已经实现)
    3. 取款(功能已经实现)
    4. 转账
    5. 账单
    6. 退出
    \033[0m'''
    menu_dic = {
        '1' : account_info,
        '2' : repay,
        '3' : withdraw,
        '4' : transfer,
        '5' : pay_back,
        '6' : logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input('>>:').strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exit!\033[0m")





def run():
    '''
    this function will be called right a way when the program started
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
       user_data['account_data'] = acc_data
       interactive(user_data)
    print("ok")

run()