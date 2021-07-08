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
from models.FundModel import FundListModel

# 自己创建的包
from views.Fund import fund

# 创建 APIRouter 实例
router = APIRouter()

# 基金列表
@router.post('/api/fund/fund_list')
async def fundList(fund_list: FundListModel):
    ''' 
    测试数据：
    {
        "uid": "1"
    }
    '''

    params = fund_list.__dict__
    print(params)
    return await fund.fundList(params['uid'])