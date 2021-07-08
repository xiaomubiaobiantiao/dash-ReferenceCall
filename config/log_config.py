'''
Description: 
Author: fanshaoqiang
Date: 2021-05-19 15:32:43
LastEditTime: 2021-05-19 15:33:07
LastEditors: fanshaoqiang
'''
from loguru import logger

logger.add('./log/server_logging_{time}.log', rotation='00:00')