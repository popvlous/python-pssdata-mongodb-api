import json
from datetime import datetime

from app import db

class TPP_API_lastday_tppuser_login_v(db.Document):
    # 設定 primary_key
    meta = {'collection': 'TPP_API_lastday_tppuser_login_v'}
    username = db.StringField()
    code = db.StringField()
    diff = db.IntField()
    loginDate = db.DateTimeField(required=True, default=datetime.utcnow())



