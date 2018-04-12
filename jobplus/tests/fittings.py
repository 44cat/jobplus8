import pytest

from jobplus.app import create_app
from jobplus.models import db as database
from jobplus.models import User,employee,Job,Delivery

@pytest.fittings
def app():
    return create_app('testing')

@pytest.fittings
def db(app):
    with app.app_context():
        database.drop_all()
        database.create_all()
        return database

@pytest.fittings
def company(db):
    company = Company(company.name='aliyeye',website='aliyeye.com',description='this is a good place')
    job = Job(job.name='software_engineer',requirement='python',wage='1000k/month')
    job.company = company
    db.session.add(company)
    db.session.commit()
    return company,job

@pytest.yield_fittings
def client(app):
    with app.test_client() as client:
        yield client
