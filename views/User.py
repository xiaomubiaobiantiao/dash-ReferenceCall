'''
@Description:
@Author: michael
@Date: 2020-12-18 16:48:20
LastEditTime: 2021-05-19 16:29:11
LastEditors: fanshaoqiang
'''
# coding=utf-8

# 加载自己创建的包

from views.user_api.UserRegister import userRegister
# from views.user_api.LoginInfo import loginInfo



# 用户接口类
class User:


    # 注册用户
    async def userRegister(self, register_params):

        return await userRegister.returnUserRegister(
            register_params['account'], 
            register_params['password'], 
            register_params['email'], 
            register_params['fund_type'], 
            register_params['fund_name'], 
            register_params['company_address'], 
            register_params['user_name']
        )


    # 返回登陆后的首页信息 lp/gp
    # async def loginInfo(self, account, password):
    #     return await loginInfo.returnLoginInfo(account, password)

    










user = User()