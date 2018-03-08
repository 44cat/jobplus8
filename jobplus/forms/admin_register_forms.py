from .base import *
from jobplus.models import db, User

class AdminRegister(FlaskForm):
    name = StringField('管理员名称',validators=[Required(),Length(3,24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    remember_me = BooleanField('记住我')
    image =  StringField('头像链接')
    submit = SubmitField('提交') 

    def create_user(self):
        user = User() #添加企业用户的普通信息
        user.name = self.name.data
        user.email = self.email.data
        user.password = self.image.data
        user.role = 30 #管理员的权限是20
        db.session.add(user)
        db.session.commit()
        return user


    def validate_name(self, field):
        if field.data and not User.query.filter_by(name=field.data).first():
            raise ValidationError('该用户名不存在')

    def validate_password(self, field):
        user = User.query.filter_by(name=self.name.data).first()
        if user and not user.check_passworld(field.data):
            raise ValidationError('密码错误')
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


class AdminProfile(FlaskForm):
    name = StringField('管理员名称',validators=[Required(),Length(2,24)])
    email = StringField('邮箱',validators=[Required(),Email(message='亲输合法的email地址')])
    password = PasswordField('密码',validators=[Required()])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    image = StringField('头像链接')
    submit = SubmitField('提交')

    def updated_profile(self,user):
        user.name = self.real_name.data
        user.email = self.email.data
        
        user.password = self.password.data
        user.logo_img = self.image.data
        db.session.add(user)
        db.session.commit()






