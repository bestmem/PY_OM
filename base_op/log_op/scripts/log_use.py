#/usr/bin/python
#coding:utf8
import logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)    #设置记录器
logger.setLevel(level=logging.WARN)     #设置日志输出级别

handler = logging.FileHandler('./output.log')    #配置处理器

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   #配置格式化器

handler.setFormatter(formatter) #为处理器设置格式

logger.addHandler(handler)  # 为记录器配置对应的处理器

logger.info('info message')
logger.debug('debug message')
logger.critical('critical message')