# __author__: Mai feng
# __file_name__: config.py
# __time__: 2019:10:30:21:07

import logging, os
from redis import StrictRedis

class Config:
    '''开启调试模式'''
    DEBUG = True
    # logging等级
    LOGGIONG_LEVEL = logging.DEBUG
    # 配置secret key,简单生成方法，ipthon 中 base64.b64encode(os.urandom(48))
    SECRET_KEY = 'ix4En7l1Hau10aPq8kv8tuzcVl1s2Zo6eA+5+R+CXor8G3Jo0IJvcj001jz3XuXl'
    #orm连接数据库
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123@127.0.0.1:3306/skin'
    # 是否开启追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置Redis数据库  待会再说
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_DB = 1
    # 配置session数据存储到redis数据库
    SESSION_TYPE = 'redis'
    # 指定存储session数据的redis的位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, )
    # 开启session数据的签名，意思是让session数据不以明文形式存储
    SESSION_USE_SIGNER = True
    # 設置session的会话的超时时长 ：一天,全局指定
    PERMANENT_SESSION_LIFETIME = 3600 * 1 # 暂定1小时

    # email配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '470957137@qq.com'
    MAIL_PASSWORD = 'tdpvjsislqskbjca'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

class DevelopConfig(Config):
    """开发阶段下的配置子类"""
    # logging等级
    LOGGIONG_LEVEL=logging.DEBUG

class UnitTestConfig(Config):
    """单元测试配置子类"""
    # logging等级
    # LOGGIONG_LEVEL = logging.DEBUG
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/project'


class ProductionConfig(Config):
    """生产环境下配置子类"""
    # logging等级
    # LOGGIONG_LEVEL = logging.WARNING
    # DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@47.106.93.190:3306/project'
    # REDIS_HOST = '47.106.93.190'
    # REDIS_PASSWORD = '123'

#工厂函数原材料
configs={
    'default'    :Config,
    'develop'    :DevelopConfig,
    'unittest'   :UnitTestConfig,
    'production' :ProductionConfig
}