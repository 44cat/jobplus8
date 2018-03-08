from .base import *
from jobplus.models import db,User,Employee
from flask import current_app


class UserRegister(FlaskForm):
    name = StringField('求职者名称',validators=[Required(),Length(2,24)])
    email = StringField('邮箱',validators=[Required(),Email(message='请输入合法email地址')])
    password = PasswordField('密码(不填写保持不变)',validators=[Required()])
    image = StringField('头像链接')
    location = StringField('城市',validators=[Required()])
    sex = SelectField('性别',validators=[Required()],choices=[('MALE','男性'),('FEMALE','女性')])
    description = TextAreaField('个人介绍',validators=[Length(10,1024)])
    resume = StringField('简历地址')
    submit = SubmitField('提交')

    def create_user(self):
        user = User() #添加用户普通信息
        user.name = self.name.data
        user.email = self.email.data
        user.password = self.password.data
        user.logo_img = self.image.data
        db.session.add(user)
        new_user = User.query.filter_by(name=user.name).first()
        employee.user = new_user
        employee.sex = self.sex.data
        employee.location = self.location.data
        employee.resume = self.resume.data
        employee.description = self.description.data
        db.session.add(employee)
        db.session.commit()
        return user

    def validate_name(self, field):
        if User.query.filter_by(name=filed.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('邮箱已经存在')

class UserProfileForm(FlaskForm):
    name = StringField('求职者名称',validators=[Required(),Length(2,24)])
    email = StringField('邮箱', validators=[Required(), Email(message='请输入合法email地址')])
    password = PasswordField('密码(不填写保持不变)',validators=[Required()])
    image = StringField('头像链接')
    sex = SelectField('性别',validators=[Required()],choices=[('MALE','男性'),('FEMALE','女性')])
    description = TextAreaField('个人介绍',validators=[Length(10,1024)])
    resume = StringField('简历地址')
    submit = SubmitField('提交')

    def update(self,user):
        # 修改企业用户信息
        user.name = self.name.data
        user.email = self.email.data
        user.password = self.password.data
        user.logo_img = self.image.data
        # 修改用户的详细信息
        employee = user.employee
        employee.description = self.description.data
        employee.location = self.location.data
        employee.sex = self.sex.data
        employee.resume = self.resume.data

        current_app.logger.debug('self.location.data: '+self.location.data)
        surrent_app.logger.debug('employee.location: '+employee.location)
        db.session.add(user)
        db.session.add(employee)
        db.session.commit()






