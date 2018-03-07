from jobplus.models import db,User,Employee,Company,Delivery
from datetime import datetime,date
import enum
from selenium import webdriver
from lxml import etree
import time
from faker import Faker
import random

def run_more():
    faker = Faker('zh-CN')
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(60)
    segmentfaulturs = ['https://segmentfault.com/companies?page='+str(i) for i in range(7)]
    for segmentfaulturl in segmentfaulturls:
        driver.get(segmentfaulturl)
        time.sleep(2)
        html = driver.page_source
        dom_tree = etree.HTML(html)
        # 获取公司的链接
        company_urls = dom_tree.xpath('//div[@class="row"]/div[@class="media"]/div[@class="col-md-9"]/div[@class="media-body"]/h4[@id="media-heading"]/a[1]/@href')
        # 获取公司的名称
        company_names = dom_tree.xpath('//div[@class="row"]/div[@class="media"]/div[@class="col-md-9"]/div[@class="media-body"]/h4[@id="media-heading"]/a/text()')
        # 获取公司图片的url
        company_logos = dom_tree.xpath('//div[@class="row"]/div[@class="media"]/div[@class="col-md-9"]/div[@class="pull-left"]/div[@class="img-warp"]/a[@class="company-logo"]/@style')
        # 获取公司网站
        company_websites = dom_tree.xpath('//div[@class="row"]/div[@class="media"]/div[@class="col-md-9"]/div[@class="media-body"]/a[@class="company-site"]/@href')
        # 获取公司一句话介绍
        company_onewords = dom_tree.xpath('//div[@class="row"]/div[@class="media"]/div[@class="col-md-9"]/div[@class="media-body"]/p[@class="company-desc"]/text()')

        for company_name in company_names:
            print(company_name)

        for company_website in company_websites:
            print(company_website)

        for company_logo in company_logos:
            print(company_logo[company_log.rfind('(')+1:company_logo.rfind(')')-1])
        
        for company_oneword in company_onewords:
            print(company_oneword)

        for company_url in company_urls:
            company_url = 'https://segmentfault.com'+company_url
            print(company_url)

        # 获取当前窗口句柄
        now_handle = driver.current_window_handle

        i = 0
        for company_url in company_urls:
            name = company_names[i]
            email = faker.email()
            password = '123456'
            logo_img = company_logos[i][company_logos[i].rfind('(')+1:company_logos][i].rfind(')')-1]
            if User.query.filter_by(name=name).first():
                # 如果企业存在就不存入数据库
                i += 1
                print('重复')
                continue
            # 把用户加入数据库
            user = User(
                    name = name,
                    email = email,
                    password = password,
                    logo_img = logo_img,
                    role = 20
            )
            db.session.add(user)
            user = User.query.filter_by(name=name).first()
            oneword = faker.sentence(nb_words=25)

            print(name)
            print(logo_img)
            print(website)
            print(oneword)

            description = faker.sentence(nb_words=50)
            # 把公司信息加入数据库
            company = Company(
                    user = user,
                    website = website,
                    oneword = oneword,
                    description = description
                    )
            db.session.add(company)
            # 给公司家入职位信息
            num = User.query.filter_by(name=name).first().id
            ran = random.randint(10,100)
            for j in range(random.randint(10,20)):
                job = Job(
                        name = faker.job(),
                        wage = str(ran)+'K - '+str(ran+10)+'K',
                        location = faker.province(),
                        company = Company.query.filter_by(user_id=num).first(),
                        description = faker.sentence(nb_words=25),
                        requirement = faker.sentence(nb_words=20)
                        )
                db.session.add(job)
                i += 1
    driver.close()
    # 向数据库提交
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
