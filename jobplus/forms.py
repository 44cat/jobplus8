from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange
from jobplus.models import db, User, CompanyDetail


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交') 

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')

class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交') 

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')


    def create_user(self):
        user = User(name=self.name.data,
                    email=self.email.data,
                    password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user


class UserProfileForm(FlaskForm):
    real_name = StringField('姓名')
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码(不填写保持不变)')
    phone = StringField('手机号')
    work_years = IntegerField('工作年限')
    resume_url = StringField('简历地址链接')
    submit = SubmitField('提交')

    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13','15','18') and len(phone) != 11:
            raise ValidationError('无效的手机号，请重新输入')

    def updated_profile(self,user):
        user.real_name = self.real_name.data
        user.email = self.email.data
        
        if self.password.data:
            user.password = self.password.data
        user.phone = self.phone.data
        user.work_years = self.work_years.data
        user.resume_url = self.resume_url.data
        db.session.add(user)
        db.session.commit()

class CompanyProfileFrom(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码(不填写保持不变)')
    slug = StringField('Slug',validators=[Length(3,24)])
    location = StringField('地址',validators=[Length(0,64)])
    site = StringField('公司网址',validators=[Length(0,64)])
    logo = StringField('Logo')
    description = StringField('一句话描述',validators=[Length(0,128)])
    about = TextAreaField('公司详情',validators=[Length(0,1024)])
    submit = SubmitField('提交')

    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13','15','18') and len(phone) != 11:
            raise ValidationError('无效的手机号，请重新输入')

    def updated_profile(self, user):
        user.name = self.name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        if user.company_detail:
            company_detail = user.company_detail
        else:
            company_detail = CompanyDetail()
            company_detail.user_id = user.id
        self.populate_obj(company_detail)
        db.session.add(user)
        db.session.add(company_detail)
        db.session.commit()

class UserEditForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码')
    real_name = StringField('姓名')
    phone = StringField('手机号')
    submit = SubmitField('提交')

    def update(self,user):
        self.populate_obj(user)
        if self.password.data:
            user.password = self.password.data
        db.session.add(user)
        db.session.commit()

class CompanyEditForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码')
    phone = StringField('手机号')
    site = StringField('公司网站',validators=[Length(0,64)])
    description = StringField('一句话简介',validators=[Length(0,128)])
    submit = SubmitField('提交')

    def update(self,company):
        company.name = self.name.data
        company.email = self.email.data
        if self.password.data:
            company.password = self.password.data
        if company.detial:
            detial = company.detial
        else:
            detial = CompanyDetial()
            detialuser_id = company.id
        detial.site = site.site.data
        detial.description = description.data
        db.session.add(company)
        db.session.add(detial)
        db.session.commit()






