'''
@Description:
@Author: michael
@Date: 2021-07-08 10:16:20
LastEditTime: 2021-07-08 20:00:00
LastEditors: michael
'''
# coding=utf-8

# 加载自己创建的包

from views.fund_api.FundList import fundList


# 基金接口类
class Fund:

    # 基金列表
    async def fundList(self, uid):
        return await fundList.returnFundList(uid)

    # 注册用户
    # async def userRegister(self, register_params):

    #     return await userRegister.returnUserRegister(
    #         register_params['account'], 
    #         register_params['password'], 
    #         register_params['email'], 
    #         register_params['fund_type'], 
    #         register_params['fund_name'], 
    #         register_params['company_address'], 
    #         register_params['user_name']
    #     )


    # 返回登陆后的首页信息
    # async def loginInfo(self, account, password):
    #     return await loginInfo.returnLoginInfo(account, password)

    










fund = Fund()