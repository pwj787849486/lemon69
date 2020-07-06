# -*- coding: utf-8 -*-
# @Time     : 2020/6/14 20:06
# @Author   : lemon_junjun
# @Email    : 787849486@qq.com

import requests

def http_request(url,data,token=None, method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Authorization':token}
    if method=='get':
        result = requests.get(url, json=data, headers=header)
    else:
        result = requests.post(url, json=data, headers=header)
    # print( result.json())
    return result.json()#return返回指定的结果

if __name__ == '__main__':
    #调用函数
    #头部
    #登录
    login_url = 'http://120.78.128.25:8766/futureloan/member/login'
    login_data = {'mobile_phone': 18971400790, 'pwd': 'pwj123456'}
    response = http_request(login_url,login_data)
    print('登录的结果是;{}'.format(response))
    # 充值
    token = response['data']['token_info']['token']
    rec_url = 'http://120.78.128.25:8766/futureloan/member/recharge'
    rec_data = {'member_id':196245, 'amount':50000}

    print(http_request(rec_url, rec_data,"Bearer "+token))

# print('充值的请求结果是:{}'.format(res))
#
# # 提现
# wit_url = 'http://120.78.128.25:8766/futureloan/member/withdraw'
# wit_data = {'member_id':userID, 'amount':50000}
# res_1 = http_requset(wit_url, wit_data, header_2)
# print('提现的请求结果是:{}'.format(res_1))
#
# # 注册
# reg_url = 'http://120.78.128.25:8766/futureloan/member/register'
# reg_data = {'mobile_phone': phoneNumber, 'pwd': pwd}
# header = {'X-Lemonban-Media-Type': 'lemonban.v2'}
# registerData = http_requset(reg_url, reg_data, header)
# mobile_phone = registerData.get('data').get('mobile_phone')