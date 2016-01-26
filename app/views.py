from flask import render_template, flash, redirect, url_for, session
from app import app, db
# from .forms import LoginForm
from .forms import RegistrationForm
from .models import Doctor
import Image
import ImageDraw
import ImageFont
from random import randint
# from flask_recaptcha import ReCaptcha
import json


def random_generator():
    sans16 = ImageFont.truetype('/Users/speedster/codes/Captcha/app/arial.ttf', 25)
    random = ''
    for i in range(6):
        r = randint(33, 122)
        random = random + chr(r)

    im = Image.new("RGB", (200, 50), "#ddd")
    draw = ImageDraw.Draw(im)
    draw.text((10, 10), random, font=sans16, fill="red")
    draw.line((0, 50, 200, 0), fill=128)
    draw.line((0, 200, 50, 0), fill=128)
    draw.line((30, 50, 200, 20), fill=128)
    # draw.line((0, 50, 200, 0), fill=128)

    im.save("/Users/speedster/codes/Captcha/app/static/mmm.png")
    return ('mmm.png?dummy='+str(randint(1, 100000)), random)


@app.route('/')
@app.route('/index')
def index():
    users = Doctor.query.all()
    return render_template('index.html',
                           title='Home',
                           users=users)


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
    if form.validate_on_submit() and form.captcha.data == session['captcha']:
        # flash('%s%s%s%s%s%s%s' % (form.first_name.data,
        #                           form.middle_name.data,
        #                           form.last_name.data,
        #                           form.gender.data,
        #                           form.birthdate.data.strftime("%d/%m/%Y"),
        #                           form.blood_group.data,
        #                           form.mobile_number.data))
        # flash('%s' % form.pincode.data)
        # flash('%s' % form.address.data)
        # flash('%s' % form.captcha.data)
        # flash('%s' % random)
        dc = Doctor(first_name=form.first_name.data,
                    middle_name=form.middle_name.data,
                    last_name=form.last_name.data,
                    gender=form.gender.data[0],
                    dob=form.birthdate.data,
                    blood_group=form.blood_group.data,
                    mobile_number=form.mobile_number.data,
                    pincode=form.pincode.data,
                    address=form.address.data,
                    city=form.city.data,
                    country=form.country.data)
        db.session.add(dc)
        db.session.commit()
        # flash(' %s %s' % (form.city.data, form.country.data))
        return redirect(url_for('index'))
    elif form.validate_on_submit() and form.captcha.data != session['captcha']:
        form.captcha.errors.append("Please enter valid captcha")
    (imgg, session['captcha']) = random_generator()
    return render_template('registration.html',
                           title='Registration Form',
                           form=form,
                           img=imgg)


@app.route('/date')
def datePicker():
    return render_template('datePicker.html')


@app.route('/recaptcha')
def reCaptcha():
    (img, session['captcha']) = random_generator()
    url = '/static/'+img
    return json.dumps({'url': url}), 200, {'Content-Type': 'application/json'}
