# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os



class Config(object):


    # mongo_host = 'mongodb://{}:{}/{}'.format(
    #     '35.221.188.167',
    #     '24017', 'pssec_test')
    #
    # MONGODB_SETTINGS = {
    #     'db': 'pssec_test',
    #     'username': 'pssec_testuser',
    #     'password': 'pssec#pw202207ya',
    #     'connect': True,
    #     'host': mongo_host,
    #     'authentication_source': 'pssec_test'
    # }


    mongo_host = 'mongodb://{}:{}/{}'.format(
        '10.140.0.12',
        '27017', 'pssec_test')

    MONGODB_SETTINGS = {
        'db': 'pssec_test',
        'username': 'pssec_testuser',
        'password': 'pssec#pw202207ya',
        'connect': True,
        'host': mongo_host,
        'authentication_source': 'pssec_test'
    }


    # MONGODB_SETTINGS = {
    #     'db': 'openfire',
    #     'username': 'openfire',
    #     'password': 'Foxconn88',
    #     'connect': True,
    #     #'host': 'mongodb://10.140.0.36:15017,10.140.0.17:15017,10.140.0.12:15017/openfire',
    #     'host': 'mongodb://192.168.100.11:15017,192.168.100.12:15017,192.168.100.13:15017/openfire',
    #     'authentication_source': 'admin'
    # }

    JOBS = [{
        'id': 'sendActionRecordJob',
        'func': 'jobs:sendActionRecordJob',
        'trigger': 'cron',
        'day': '*',
        'hour': 16,
        'minute': 30,
        'second': 10,
    }]

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
        'day': '*',
        'hour': 16,
        'minute': 30,
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
