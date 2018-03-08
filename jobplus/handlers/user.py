from flask import Blueprint,render_template,flash,redirect,url_for
from flask import current_app,request
from flask_login import login_required,current_user,login_user,logout_user
from jobplus.models import User
from jobplus.forms import UserRegister,CompanyRegister,AdminRegister,UserProfile,AdminProfile,CompanyProfile

user = Blueprint('user',__name__,url_prefix='/user')

# 修改求职者用户的信息
@user.route('/user_profile',methods=['GET','POST'])
@login_required
def user_profile():
    form = UserProfile()
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('简历更新成功','success')
        return redirect(url_for('user.user_profile'))
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.image.data = current_user.logo_img
    form.sex.data = current_user.employee.sex.name
    form.location.data = current_user.employee.location
    form.description.data = current_user.employee.description
    form.resume.data = current_user.employy.resume
    return render_template('user/profile.html',form=form,user=current_user)

# 修改管理员信息
@user.route('/admin_profile',methods=['GET','POST'])
@login_required
def admin_profile():
    form = AminProfile()
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash('简历更新成功','success')
        return redirect(url_for('user.admin_profile'))
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.image.data = current_user.logo_img
    return render_template('profile.html',form=form,user=current_user)

# 修改企业用户的信息
@user.route('/company_profile',methods=['GET','POST'])
@login_required
def admin_profile():
    form = CompanyProfile()
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash('简历更新成功','success')
        return redirect(url_for('user.company_profile'))
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.image.data = current_user.logo_img
    form.web.data = current_user.company.website
    form.oneword.data = current_user.company.oneword
    form.description.data = current_user.company.description
    return render_template('profile.html',form=form,user=current_user)
