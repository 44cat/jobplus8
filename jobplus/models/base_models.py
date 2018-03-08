from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()

class Base(db.Model):
    # 表示不要把这个类当作Model类
    __abstract__ = True
    # 设置了 default 和 onupdate 这两个时间戳都不需要自己维护
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

