from instance import db
class Address(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    users = db.relationship('User', backref = "address", lazy=True)