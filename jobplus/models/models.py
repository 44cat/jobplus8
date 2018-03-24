from flask import url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .base_models import db,Base

class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_EMPLOYEE = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    logo_img = db.Column(db.String(128))
    # 连接到公司的关系为1-1
    company = db.relationship('Company',uselist=False)
    # 连接到求职者的关系为1-1
    employee = db.relationship('Employee',uselist=False)
    role = db.Column(db.SmallInteger, default=ROLE_EMPLOYEE)
    #根据用户在网站上填写的内容生成的简历

    def __repr__(self):
        return '<User:{}>'.format(self.name)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY
    
    @property
    def is_staff(self):
        return self.role == self.ROLE_EMPLOYEE

import enum
class SexType(enum.Enum):
    NONE = 0
    MALE = 1
    FEMALE = 2

# 求职者表
class Employee(Base):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    sex = db.Column(db.Enum(SexType),default=SexType.NONE)
    location = db.Column(db.String(128))
    user = db.relationship('User',uselist=False,backref=db.backref('user_detail',uselist=False))
    description = db.Column(db.String(256))
    resume = db.Column(db.String(128))

# 企业表
class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),index=True)
    user = db.relationship('User',uselist=False)
    website = db.Column(db.String(64))
    #一句话描述
    oneword = db.Column(db.String(128))
    #关于我们，公司详情描述
    description = db.Column(db.String(256))
    #公司技术栈,多个用逗号隔开,最多10个
    stack = db.Column(db.String(128))
    #团队介绍
    team_introduction = db.Column(db.String(256))
    #公司福利
    welfares = db.Column(db.String(256))
    #公司领域
    field = db.Column(db.String(256))
    #融资进度
    finance_stage = db.Column(db.String(128))

    @property
    def url(self):
        return url_for('company.detail',company_id=self.id)

# 职位表
class Job(Base):
    __tablename__ = 'job'
    
    id = db.Column(db.Integer,primary_key=True)
    #职位名称
    name = db.Column(db.String(64))
    wage = db.Column(db.String(64))
    location = db.Column(db.String(64))
    description = db.Column(db.String(256))
    company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='CASCADE'))
    company = db.relationship('Company', uselist=False)
    requirement = db.Column(db.String(256))
    is_disable = db.Column(db.Boolean,default=False)

    @property
    def url(self):
        return url_for('job.detail',job_id = self.id)

    @property
    def apply(self):
        return url_for('job.apply',job_id = self.id)

    @property
    def login(self):
        return url_for('front.login',job_id = self.id)

    @property
    def current_user_is_applied(self):
        d = Delivery.query.filter_by(job_id=self.id,user_id=current_user.id).first()
        return (d is not None)

class Qualify_Type(enum.Enum):
    UNREAD = 0 # 未被阅读
    READ = 1 # 已被阅读
    REFUSE = 2 # 拒绝该简历
    ACCEPT =3 # 接受该简历

# 投递表
class Delivery(Base):
    __tablename__ = 'delivery'

    id = db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    user = db.relationship("User")
    employee_id = db.Column(db.Integer,db.ForeignKey('employee.id'))
    resume = db.relationship('Employee')
    job = db.relationship('Job')
    
    #企业回应
    qualify = db.Column(db.Enum(Qualify_Type),default = Qualify_Type.UNREAD)


    



