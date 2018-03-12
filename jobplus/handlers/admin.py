from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from flask_login import login_user,logout_user,login_required
from jobplus.decorators import admin_required
from jobplus.models import User,Job
from jobplus.forms import UserRegister,CompanyRegister,AdminRegister,UserProfile,AdminProfile,CompanyProfile


admin = Blueprint('admin', __name__, url_prefix='/admin')

# 用户管理界面
@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

# 管理用户
@admin.route('/users')
@admin_required
def users():
    page = request.args.get('page',default=1,type=int)
    pagination = User.query.pagination(
            page,per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out=False
            )
    return render_template('admin/users.html',pagination=pagination)

# 管理职位
@admin.route('/jobs')
@admin_required
def jobs():
    page = request.args.get('page',default=1,type=int)
    pagination = Job.query.pagination(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
        )
    return render_template('admin/jobs.html',pagination=pagination)
    


# 增加用户
@admin.route('/users/adduser',methods=['GET','POST'])
@admin_required
def create_user():
    form = UserRegister()
    if form.is_submitted():
        form.create_user()
        flash('用户创建成功','success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_user.html',form=form)

# 增加企业
@admin.route('/users/addcompany',methods=['GET','POST'])
@admin_required
def create_company():
    form = CompanyRegister()
    form.name.label = u'企业名称'
    if form.validate_on_submit():
        form.create_user()
        flash('企业创建成功','success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_company.html',form=form)

# 修改求职者用户信息
@admin.route('/user_profile/<int:user_id>',methods=['GET','POST'])
@login_required
def user_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    form = UserProfile()
    if form.validate_on_submit():
        form.update_profile(user)
        flash('简历更新成功','success')
        return redirect(urlfor('admin.user_profile',user_id=user_id))
    form.name.data = user.name
    form.email.data = user.email
    form.image.data = user.logo_img
    form.sex.data = user.employee.sex.name
    form.description.data = user.employee.description
    form.resume.data = user.employee.resume
    return render_template('admin/profile.html',form=form,user=user)

# 修改管理员信息
@admin.route('/admin_profile/<int:user_id>',methods=['GET','POST'])
@login_required
def admin_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    form = AdminProfile()
    if form.validate_on_submit():
        form.update_profile(user)
        flash('简历更新成功','success')
        return redirect(urlfor('user.admin_profile',user_id=user_id))
    form.name.data = user.name
    form.email.data = user.email
    form.image.data = user.logo_img
    return render_template('admin/profile.html',form=form,user=user)

# 修改企业用户信息
@admin.route('/company_profile/<int:user_id>',methods=['GET','POST'])
@login_required
def company_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    form = CompanyProfile()
    if forms.validate_on_submit():
        forms.update_profile(user)
        flash('简历更新成功','success')
        return redirect(urlfor('user.company_profile',user_id=user_id))
    form.name.data = user.name
    form.email.data = user.email
    form.image.data = user.logo_img
    form.web.data = user.company.website
    form.oneword.data = user.company.oneword
    form.description.data = user.employee.description
    return render_template('admin/profile.html',form=form,user=user)


# 禁用页面
@admin.route('/users/<int:user_id>/disable',methods=['GET','POST'])
@admin_required
def disable_user(user_id):
    user =  User.query.get_or_404(user_id)
    if user.is_disable:
        user.is_disable = False
        flash('已经成功禁用用户','success')
    else:
        user.is_disable = False
        flash('已经成功禁用用户','success')
    db.session.add(user)
    db.session.commit()
    return redirect(urlfor('admin.users'))
