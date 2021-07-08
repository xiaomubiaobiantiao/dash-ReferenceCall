'''
@Description:
@Author: michael
@Date: 2021-07-08 10:16:20
LastEditTime: 2021-07-08 20:00:00
LastEditors: michael
'''
# coding=utf-8

# 加载第三方包
# from bson.objectid import ObjectId

# 加载自己创建的包
from common.register_class import *
from config.log_config import logger

class Base:

    # 根据 id 验证是否有此用户
    async def verifyUser(self, uid=''):

        # 连接数据库
        dbo.resetInitConfig('referencecall', 'users')

        # 条件 - 用户名 - 返回字段 全部
        condition = {'id': uid}
        field = {'id':1, '_id': 0}
        result = await dbo.findOne(condition, field)
        
        if result is None:
            return False

        return True







base = Base()

