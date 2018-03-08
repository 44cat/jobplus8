from flask import Blueprint,render_template,redirect,url_for,flash,current_app,request
from jobplus.models import User,Job,Company
from jobplus.forms import UserRegister,LoginForm,CompanyRegister
from jobplus.config import configs
from flask_login import login_user,logout_user,login_required
from flask_migrate import Migrate

front = Blueprint('front', __name__)

# 主页
@front.route('/')
def index():
    jobs = Job.query.order_by(Job.description).limit(8)
    companies = Company.query.order_by(Company.description.desc()).limit(8)
    return render_template(
            'front/index.html',
            active = 'base',
            newest=[jobs,companies],
            hot=[jobs,companies]
            )

# 用户注册页
@front.route('/userregister', methods=['GET', 'POST'])
def user_register():
    form = RegisterForm()
    try:
        form.validate_on_submit()
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login')) # 注册成功则自动跳转到登录页
    except:
        flash('注册失败,请重新注册','warning')
    return render_template('front/register_user.html', form=form)

# 公司注册页
@front.route('/companyregister', methods=['GET', 'POST'])
def company_register():
    form = CompanyRegisterForm()
    try:
        form.validate_on_submit()
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    except:
        flash('注册失败,请重新注册','warning')
    return render_template('front/register_company.html',form=form)

# 登录页
@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
#        if user.is_disable:
#            flash('该用户已经被禁用',"Danger")
#            return redirect(url_for('front.login',form=form))
#        else:
#            login_user(user, form.remember_me.data)
#            lash("终于等到你"+form.name.data+"登录","success")
#            return redirect(url_for('front.index'))
        login_user(user, form.remember_me.data)
        flash("终于等到"+ form.name.data+"你光临啦","success")
        return redirect(url_for('front.index'))
        
        if user.is_admin:
            return redirect(url_for('admin.user'))
        elif user.is_company:
            return redirect(url_for('company.profile'))
        else:
            return redirect(url_for('user.profile'))
    else:
        return render_template('front/login.html', form=form)

# 退出页
@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('.index'))

