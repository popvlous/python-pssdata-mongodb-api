import json
from datetime import datetime
from sqlalchemy import DateTime

#from app import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class TPP_API_lastday_tppuser_login_v(db.Document):
#     # 設定 primary_key
#     meta = {'collection': 'TPP_API_lastday_tppuser_login_v'}
#     username = db.StringField()
#     code = db.StringField()
#     diff = db.IntField()
#     loginDate = db.DateTimeField(required=True, default=datetime.utcnow())


class CovidInfo(db.Model):
    """
        covid info 表
    """
    __tablename__ = 'interaction_web_covid_info'
    id = db.Column(db.Integer, primary_key=True)
    total_deaths = db.Column(db.String(128))  # 死亡數量
    daily_deaths_tw = db.Column(db.String(128))  # 每日死亡數量
    total_cases = db.Column(db.String(128))  # 累積確診
    daily_cases = db.Column(db.String(128))  # 每日確診
    total_cases_tw = db.Column(db.String(128))  # 本土累積確診
    daily_cases_tw = db.Column(db.String(128))  # 本土每日確診
    update_time = db.Column(DateTime, default=datetime.utcnow)  # 更新時間
    tw_vaccinated = db.Column(db.String(128))  #累積疫苗
    dose1st = db.Column(db.String(128))  # 第一劑
    dose2st = db.Column(db.String(128))  # 第二劑

    def __init__(self, id, total_deaths, daily_deaths_tw, total_cases, daily_cases, total_cases_tw, daily_cases_tw, tw_vaccinated, dose1st, dose2st):
        self.id = id
        self.total_deaths = total_deaths
        self.daily_deaths_tw = daily_deaths_tw
        self.total_cases = total_cases
        self.daily_cases = daily_cases
        self.total_cases_tw = total_cases_tw
        self.daily_cases_tw = daily_cases_tw
        self.tw_vaccinated = tw_vaccinated
        self.dose1st = dose1st
        self.dose2st = dose2st