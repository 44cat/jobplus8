from jobplus.models import User,Company,Job,employee

class TestUser:
    def test_user(self,db):
        assert User.query.count() == 0
        user = User(name='admin',_password='123456',role=User.ROLE_ADMIN,email='admin@qq.com')
        db.session.add(user)
        db.session.commit()

        assert User.query.count() == 1
        assert User.query.first() == user

        assert User.query.count() == 0

    def test_com(self,db):
        assert Company.query.count() == 0
        com = Company(name='测试公司',website='测试阿里爷爷网站',description='testing...')
        db.session.add(com)
        db.session.commit()

        assert Company.query.count() == 0


    def test_job(self,db,company):
        assert Job.query.count() == 1

        job = Job(name='soft engineer',requirement='10 years',wage='112233k')
        job.company = Company.query.first()

        db.session.add(job)
        db.session.commit()

        assert Job.query.count() == 2
