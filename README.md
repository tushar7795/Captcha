# Captcha
Implemented Doctor registration form using Flask micro-framework and extension Flask-WTForms which also validates input using validators provided by wtforms.I also implemented my own captcha using Python Imaging Library(PIL). Flask-sqlalchemy extension has been used as ORM to connect with mySql database and Database migration is implemented using extension sqlalchemy-migrate. 

# Prerequisite
virtualenv

Python

Python Imaging Library(PIL)

# Setup
create virtual environment in the folder in which you want to clone the project.
```shell
$ virtualenv flask
```
Then activate the virtual environment using following command:
```shell
$ source flask/bin/activate
```
Now install Flask and necessary extensions using following command: 
```shell
(flask) $ pip install flask
(flask) $ pip install flask-sqlalchemy
(flask) $ pip install sqlalchemy-migrate
(flask) $ pip install flask-wtf
(flask) $ pip install flask-bootstrap
```

Then clone this project using following command:
```git
$ git clone https://github.com/tushar7795/Captcha.git
```

# Usage
First add excution permission to *run.py*.
```shell
$ chmod a+x run.py
```
Now you can run server by running only *run.py*.
```shell
$ ./run.py
```

Now open [http://localhost:5000/registration](http://localhost:5000/registration) in your browser to open registration form. 

