# -*- coding: utf-8 -*-
# @Time     : 2020/6/14 20:06
# @Author   : lemon_junjun
# @Email    : 787849486@qq.com
from LEMON69.R_W_excel import read_data
from LEMON69.http_request import http_request
#执行文件
#获取到所有的测试数据a

all_case=read_data('test_case.xlsx', 'recharge')
print("所有的测试数据为：",all_case)

print("第一条测试数据为：",all_case[0])
log_data = all_case[0]
ip="http://120.78.128.25:8766"
log_response = http_request(ip + log_data[4], eval(log_data[5]), token=None, method=log_data[3])
for i in range(len(all_case)):
    test_data = all_case[i]
    token=log_response['data']['token_info']['token']
    response=http_request(ip+test_data[4],eval(test_data[5]),token="Bearer "+token,method=test_data[3])
    expected = eval(test_data[6])
    print("最后的结果值：",response)