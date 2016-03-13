import os
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:@localhost/captcha'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_SUBJECT_PREFIX = '[Captcha]'
MAIL_SENDER = 'Tushar Santoki<tushar.santoki@practo.com>'

# RECAPTCHA_OPTIONS = {'theme': 'red'}
# You can change the theme -- >
# https://developers.google.com/recaptcha/docs/customization
RECAPTCHA_PUBLIC_KEY = "6LeLhRUTAAAAABaU-jgfnYl8FwktJCyBZDPZXhT0"
# https://www.google.com/recaptcha
RECAPTCHA_PRIVATE_KEY = "6LeLhRUTAAAAAMZwo-w3xASuFw2FqXfOuGXEEbMr"
# https://www.google.com/recaptcha
