from .base import *
from jobplus.models import db,User,Employee,Company

class UserProfile(FlaskForm):
    name = StringField('求职者名称',validators=[Required(),Length(2,24)])
    email = StringField('邮箱',validators=[Required(),Email(message='请输入合法email地址')])
    password = PasswordField('密码(不填写保持不变)',validators=[Required()])
    image = StringField('头像链接')
    location = StringField('城市',validators=[Required()])
    sex = SelectField('性别',validators=[Required()],choices=[('MALE','男性'),('FEMALE','女性')])
    description = TextAreaField('个人介绍',validators=[Length(10,1024)])
    resume = StringField('简历地址')
    submit = SubmitField('提交')

    def updata_profile(self,user):
        #添加用户普通信息
        user.name = self.name.data
        user.email = self.email.data
        user.password = self.password.data
        user.logo_img = self.image.data
        db.session.add(user)
        employee = user.employee
        employee.sex = self.sex.data
        employee.location = self.location.data
        employee.resume = self.resume.data
        employee.description = self.description.data
        db.session.add(employee)
        db.session.commit()

class CompanyProfile(FlaskForm):
    name = StringField('企业名称',validators=[Required(),Length(2,24)])
    email = StringField('邮箱', validators=[Required(), Email(message='请输入合法email地址')])
    password = PasswordField('密码(不填写保持不变)',validators=[Required()])
    image = StringField('头像链接')
    oneword = StringField('一句话介绍',validators=[Required()])
    description = TextAreaField('企业介绍',validators=[Length(10,1024)])
    submit = SubmitField('提交')

    def updateprofile(self,company):
        # 修改企业用户信息
        company.name = self.name.data
        company.email = self.email.data
        if self.password.data:
            company.password = self.password.data
        if company.user_detail:
            user_detail = company.user_detail
        else:
            user_detail = Employee()
            user_detail.user_id = company.id
        self.populate_obj(user_detail)
        db.session.add(user_detail)
        db.session.add(company)
        db.session.commit()






