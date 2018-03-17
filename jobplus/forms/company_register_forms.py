from .base import *
from jobplus.models import db,User,Company 


class CompanyRegister(FlaskForm):
    name = StringField('企业名称',validators=[Required(),Length(2,24)])
    email = StringField('邮箱',validators=[Required(),Email(message='请输入合法email地址')])
    password = PasswordField('密码(不填写保持不变)',validators=[Required()])
    website = StringField('公司网址',validators=[Length(0,64)])
    logo = StringField('Logo')
    image = StringField('头像链接')
    oneword = StringField('一句话描述',validators=[Length(0,128)])
    description = TextAreaField('公司详情',validators=[Length(10,1024)])
    submit = SubmitField('提交')

    def create_user(self):
        user = User() #添加企业用户普通信息
        user.name = self.name.data
        user.email = self.email.data
        user.password = self.password.data
        user.logo_img = self.image.data
        user.role = 20
        db.session.add(user)
        new_user = User.query.filter_by(name=user.name).first()
        company = Company()
        company.user = new_user
        company.oneword = self.oneword.data
        company.website = self.website.data
        company.description = self.description.data
        db.session.commit()
        return user

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class CompanyProfile(FlaskForm):
    name = StringField('企业名称',validators=[Required(),Length(2,24)])
    email = StringField('邮箱', validators=[Required(), Email(message='请输入合法email地址')])
    password = PasswordField('密码(不填写保持不变)',validators=[Required()])
    website = StringField('公司网站',validators=[Required()])
    image = StringField('头像链接')
    oneword = StringField('一句话简介',validators=[Length(0,128)])
    description = TextAreaField('公司详情',validators=[Length(10,1024)])
    submit = SubmitField('提交')

    def update(self,user):
        # 修改企业用户信息
        user.name = self.name.data
        user.email = self.email.data
        user.password = self.password.data
        user.logo_img = self.image.data
        # 修改用户的详细信息
        company = user.company
        company.website = self.website.data
        company.description = self.description.data
        comapny.oneword = self.oneword.data
        db.session.add(user)
        db.session.add(company)
        db.session.commit()






