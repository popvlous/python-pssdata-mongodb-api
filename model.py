import json
from datetime import datetime

from app import db

# class TPP_API_lastday_tppuser_login_v(db.Document):
#     # 設定 primary_key
#     meta = {'collection': 'TPP_API_lastday_tppuser_login_v'}
#     username = db.StringField()
#     code = db.StringField()
#     diff = db.IntField()
#     loginDate = db.DateTimeField(required=True, default=datetime.utcnow())


class CovidInfo(db.Document):
    """
        信用卡非同步回調表
    """
    meta = {'collection': 'CovidInfo'}
    total_deaths = db.StringField()  # 死亡數量
    daily_deaths_tw = db.StringField() # 每日死亡數量
    total_cases = db.StringField()  # 累積確診
    daily_cases = db.StringField()  # 每日確診
    total_cases_tw = db.StringField()  # 本土累積確診
    daily_cases_tw = db.StringField()  # 本土每日確診
    update_time = db.DateTimeField(required=True, default=datetime.utcnow())  # 更新時間
    tw_vaccinated = db.StringField()  #累積疫苗
    dose_1st = db.StringField()  # 第一劑
    dose_2st = db.StringField()  # 第二劑

