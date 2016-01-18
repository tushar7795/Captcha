from flask.ext.wtf import Form
from flask.ext.wtf.recaptcha import RecaptchaField
from wtforms import StringField, IntegerField, RadioField, SelectField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import DateField

# from flask_recaptcha import ReCaptcha


class RegistrationForm(Form):
    blood_types = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
                   ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')]
    first_name = StringField('first_name', validators=[DataRequired()])
    middle_name = StringField('middle_name', validators=[])
    last_name = StringField('last_name', validators=[DataRequired()])
    gender = RadioField('gender', choices=[('male', 'male'),
                                           ('female', 'female')])
    birthdate = DateField('birthdate')
    blood_group = SelectField('blood_group', choices=blood_types,
                              validators=[DataRequired()])
    mobile_number = IntegerField('mobile_number', validators=[NumberRange(
                                7000000000,
                                9999999999,
                                '''valid number in india starts with 7,8,9
                                and Mobile Number must be of 10 digits''')])
    pincode = IntegerField('pincode',
                           validators=[NumberRange(
                            100000,
                            999999,
                            "pincode must be of 6 digits")])
    city = StringField('city', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    address = TextAreaField('address', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
    captcha = StringField('captcha', validators=[DataRequired()])


    # recaptcha = ReCaptcha()
    # remember_me = BooleanField('remember_me', default=False)
