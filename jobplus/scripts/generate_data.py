from jobplus.models import db,User,Employee,Company,Job,Delivery
from datetime import datetime,date
import enum
import os
import json

# 生成一个管理员,一个求职者,一个企业用户
def iter_users():
    yield User(
        name='admin',
        email = 'admin@qq.com',
        password = '123456',
        logo_img = 'https://avatars2.githubusercontent.com/u/26021510?s=400&v=4',
        role = 30
    )
    # 创建企业用户
    yield User(
        name='company',
        email = 'company@qq.com',
        password = 'company',
        logo_img = 'https://avatars2.githubusercontent.com/u/26021510?s=400&v=4',
        role = 20
    )
    # 创建求职者
    yield User(
        name = 'user',
        email = 'user@qq.com',
        password = 'user',
        logo_img = 'https://avatars2.githubusercontent.com/u/26021510?s=400&v=4',
        role = 10
    )

# 生成求职者的信息
class SexType(enum.Enum):
    NONE = 0
    MALE = 1
    FEMALE = 2

def iter_employee():
    yield Employee(
        user = User.query.filter_by(name='user').first(),
        # sex = SexType.MALE,
        location = '金银岛',
        description = '大家好',
        resume = 'url'
    )

# 生成企业的信息
def iter_company():
    yield Company(
        user = User.query.filter_by(name='company').first(),
        website = 'https://www.lagou.com/',
        oneword = '这里是企业的介绍',
        description = '这是一家有着百年历史的企业',
        stack = 'Python',
        team_introduction = '猫猫天团',
        welfares = '送美人一只猫',
        field = '养猫',
        finance_stage = 'E轮融资'
    )
            
# 生成职位表的信息
def iter_job():
    num = User.query.filter_by(name='company').first().id
    print(num)
    yield Job(
        name = '工程师',
        wage = '80万/月',
        location = '金银岛',
        company = Company.query.filter_by(user_id=num).first(),
        description = '我们需要招的是工程师',
        requirement = '我们需要招有10年的工作经验的人'
    )

def iter_jobs():
    user = User.query.filter_by(name='user').first()
    # with open(os.path.join(os.path.dirname(__file__),'datas','job.json')) as f:
    with open(os.path.join(os.path.dirname(__file__),'datas','job.json')) as f:
        jobs = json.load(f)
    for job in jobs:
        yield Job(
                name = job['name'],
                #location = job['location'],
                #wage = job['wage'],
                #description = job['description'],
                #qualifications = job['qulications'],
                #experience = job['experience'],
                #work_time = job['work_time']
            )
# 生成投递表
class Qualify_Type(enum.Enum):
    UNREAD = 0 #未被阅读
    READ = 1 #已被阅读
    REFUSE = 2 #拒绝该简历
    ACCEPT = 3 #接受该简历

def iter_delivery():
    num = User.query.filter_by(name='company').first().id
    company_id = Company.query.filter_by(user_id=num).first()
    yield Delivery(
            company_id = company_id.id,
            # 投递的工作需要根据职位和公司id确定
            #job_id = Job.query.filter_by(name='工程师',company_id=company_id).first().id,
            employee_id = Employee.query.filter_by(user_id = User.query.filter_by(name='user').first().id).first().id,
            qualify = 'UNREAD'
    )

def run():
    for user in iter_users():
        db.session.add(user)
    
    for employee in iter_employee():
        db.session.add(employee)

    for company in iter_company():
        db.session.add(company)

    for job in iter_job():
        db.session.add(job)

    for delivery in iter_delivery():
        db.session.add(delivery)

    try:
        db.session.commit()
    except Exception as e:
        print('--------------------')
        print(e)
        db.session.rollback()
