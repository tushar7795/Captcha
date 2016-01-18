from flask import render_template, flash, redirect, session, url_for, request
from flask import g
from flask.ext.login import login_user, logout_user, current_user
from flask.ext.login import login_required
from app import app, db
# from .forms import LoginForm
from .forms import RegistrationForm
from .models import User
# from flask_recaptcha import ReCaptcha


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


# @app.route('/login', methods=['GET', 'POST'])
# @oid.loginhandler
# def login():
#     if g.user is not None and g.user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['remember_me'] = form.remember_me.data
#         return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
#     return render_template('login.html',
#                            title='Sign In',
#                            form=form,
#                            providers=app.config['OPENID_PROVIDERS'])


@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('%s%s%s%s%s%s%s' % (form.first_name.data,
                                  form.middle_name.data,
                                  form.last_name.data,
                                  form.gender.data,
                                  form.birthdate.data.strftime("%d/%m/%Y"),
                                  form.blood_group.data,
                                  form.mobile_number.data))
        flash('%s' % form.pincode.data)
        flash('%s' % form.address.data)
        flash(' %s %s' % (form.city.data, form.country.data))
        return redirect(url_for('index'))
    return render_template('registration.html',
                           title='Registration Form',
                           form=form)


@app.route('/date')
def datePicker():
    return render_template('datePicker.html')
