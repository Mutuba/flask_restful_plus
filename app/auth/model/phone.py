from instance import db
from app.auth.model import user
class Phone(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "phone"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
