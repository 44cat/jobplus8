import random
import requests
from faker import Faker 
from jobplus.models import db,User,CompanyDetail,Job

fake = Faker('zh_CN')

class LagouSpider(object):
    url = 'https://www.lagou.com/gongsi/0-0-0.json'

    @property
    def headers(self):
        return {
                'Accept':'application/json,text/java/javascript,*/*;q=0.01',
                'Accept-Encoding':'gzip,deflate,br',
                'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
                'Host':'www.lagou.com',
                'Origin':'https://www.lagou.com',
                'Referer':'https://www.lagou.com/gongsi/',
                'User-Agent':'Mozilla/5.0 (Macintiosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/62.0.3202 Safari/537.36',
                'X-Anit-Forge-Code':'0',
                'X-Anit-Forge-Token':'None',
                'X-Request-With':'XMLHttpRequest'
                }
    def formdata(self,page):
        return {
                'first':False,
                'pn':page,
                'sortField':0,
                'havemark':0
                }

    @property
    def company(self):
        for page in range(2,4):
            r = request.get(self.url,headers=self.headers,data=self.formdata(page))
            result = r.json()['result']
            for company in result:
                yield company

class FakerData(object):
    def __init__(self):
        self.lagou = LagouSpider()

    def fake_company(self):
        for company in self.lagou.company:
            c = User(
                    name=company['companyShortName'],
                    email=fake.email(),
                    role=User.ROLE_COMPANY
                    )
            c.password = '123456'
            db.session.add(c)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                continue
            d = CompanyDetail(
                    logo='https://static.lagou.com/thumbnail_160x160' + company['companyLogo'],
                    site='https://shiyanlou.com',
                    location=company['city'],
                    field=company['industryField'],
                    finace_stage=company['financeStage']
                    )
            d.user_id = c.id
            db.session.add(d)
            db.session.commit()

if __name__ == '__main__':
    f = FakerData()
    f.fake_company()
