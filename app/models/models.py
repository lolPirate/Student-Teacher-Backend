from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email_primary = db.Column(db.String(1000), unique=True, nullable=False)
    phone_primary = db.Column(db.String(1000), unique=True, nullable=False)
    profile = db.relationship('Profile', backref='person', uselist=False)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    email_secondary = db.Column(db.String(1000), nullable=True)
    phone_secondary = db.Column(db.String(1000), nullable=True)
    region = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(1000), nullable=True)
    state = db.Column(db.String(1000), nullable=True)
    city = db.Column(db.String(1000), nullable=True)
    zip_code = db.Column(db.String(1000), nullable=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
