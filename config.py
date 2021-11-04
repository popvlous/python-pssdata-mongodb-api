# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import pymysql

pymysql.install_as_MySQLdb()


class Config(object):

    MONGODB_SETTINGS = {
        'db': 'openfire',
        'username': 'openfire',
        'password': 'Foxconn88',
        'connect': True,
        #'host': 'mongodb://10.140.0.36:15017,10.140.0.17:15017,10.140.0.12:15017/openfire',
        'host': 'mongodb://192.168.100.11:15017,192.168.100.12:15017,192.168.100.13:15017/openfire',
        'authentication_source': 'admin'
    }

    JOBS = [{
        'id': 'sendActionRecordJob',
        'func': 'jobs:sendActionRecordJob',
        'trigger': 'interval',
        'seconds': 10
    }]

    # JOBS = [{
    #     'id': 'sendActionRecordJob',
    #     'func': 'jobs:sendActionRecordJob',
    #     'trigger': 'cron',
    #     'day_of_week': '*',
    #     'hour': 16,
    #     'minute': 17,
    #     'second': 10,
    # }]

    SCHEDULER_TIMEZONE = 'Asia/Shanghai'  # 配置時區

    DOMAIN_URL = 'https://member-api.tpp.org.tw/'
    DATA_TOKEN = 'ENXsCAbfyXYqincPulKe'

    LINE_TOKEN = 'qUYZTP3u08ugL8mCGJNSKJis45VlHO3RnjWdCuWUcoZ'

    SCHEDULER_API_ENABLED = True  # 新增API


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    MONGODB_SETTINGS = {
        'db': 'openfire',
        'username': 'openfire',
        'password': 'Foxconn88',
        'connect': True,
        'host': 'mongodb://10.140.0.36:15017,10.140.0.17:15017,10.140.0.12:15017/openfire',
        #'host': 'mongodb://192.168.100.11:15017,192.168.100.12:15017,192.168.100.13:15017/openfire',
        'authentication_source': 'admin'
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }

    JOBS = [{
        'id': 'sendActionRecordJob',
        'func': 'jobs:sendActionRecordJob',
        'trigger': 'cron',
        'day_of_week': '*',
        'hour': 5,
        'minute': 1,
        'second': 10,
    }]

    SCHEDULER_TIMEZONE = 'Asia/Shanghai'  # 配置時區

    DOMAIN_URL = 'https://member-api.tpp.org.tw/'
    DATA_TOKEN = 'ENXsCAbfyXYqincPulKe'

    LINE_TOKEN = 'qUYZTP3u08ugL8mCGJNSKJis45VlHO3RnjWdCuWUcoZ'

    SCHEDULER_API_ENABLED = True  # 新增API



class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
