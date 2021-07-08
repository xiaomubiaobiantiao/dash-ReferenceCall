'''
@Description:
@Author: michael
@Date: 2020-12-09 19:48:20
LastEditTime: 2020-12-11 20:00:00
LastEditors: michael
'''
# coding=utf-8

# 第三方包
from fastapi import APIRouter
from models.UserModel import UserRegisterModel
# from models.UserModel import UserLoginModel

# 自己创建的包
from views.User import user

# 创建 APIRouter 实例
router = APIRouter()

# 注册
@router.post('/api/user/register')
async def userRegister(register_params:UserRegisterModel):
    '''
    1. 账号只可以用邮箱来注册 - email 是添加 account 后自动同步的字段
    2. 测试的时候最好用一个可以接收邮件的邮箱来注册
    3. 注册后会发送验证码邮件到注册账号，然后添加验证码，认证后才可以正常登陆
    4. 第一个注册公司的人会是管理身份，不需要审核就可以登陆，后面相同公司名称的人员注册并验证成功后需要管理员审核，才可以正常登陆
    '''
    params = register_params.__dict__
    print(params)
    return await user.userRegister(params)

# 用户登陆后的首个返回信息
# @router.post('/api/user/login')
# async def loginFirstInfo(login_params:UserLoginModel):
#     ''' 测试数据
#     {
#         "account":"1",
#         "password":"1"
#     }
#     '''

#     params = login_params.__dict__
#     return await user.loginInfo(params['account'], params['password'])
