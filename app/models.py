from app import db


class Doctor(db.Model):
    __tablename__ = 'doctor_info'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    middle_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    dob = db.Column(db.Date(), nullable=False)
    blood_group = db.Column(db.String(3), nullable=False)
    mobile_number = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.first_name)
