from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Zipcode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30))
    state = db.Column(db.String(15))
    longitude = db.Column(db.String(25))
    latitude = db.Column(db.String(25))
    population = db.Column(db.String(15))
    zip_code = db.Column(db.String(15))

    def __repr__(self):
        return '<Zipcode %r>' % self.city

    def serialize(self):
        return {
            "city": self.city,
            "state": self.state,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "population": self.population,
            "zip": self.zip_code
        }