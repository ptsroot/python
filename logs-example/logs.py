# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：        logs
   Description :
   Author :           chenchaoyin
   date：             2019/10/28
-------------------------------------------------
   Change Activity:   2019/10/28:
-------------------------------------------------
"""
import logging
import os
from logging.handlers import RotatingFileHandler
if not os.path.exists(os.path.dirname(__file__) + "/logs"):
    os.mkdir(os.path.dirname(__file__) + "/logs")

log_file_name = './logs/log.logs'

logging.basicConfig(level=logging.INFO)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler(log_file_name, maxBytes=1024 * 1024 * 100,
                                       backupCount=10)

console_handler = logging.StreamHandler()

# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)-2s Line:%(lineno)-d: %(message)s', '%Y-%m-%d %H:%M:%S')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logger = logging.getLogger()
logger.addHandler(file_log_handler)
logger.addHandler(console_handler)
