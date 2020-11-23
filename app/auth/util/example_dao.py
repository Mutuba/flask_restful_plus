from app.models import User
from app.db import session
class UserDAO:
    def __init__(self, model):
        self.model = model    
    
    def get_all(self):
        return session.query(self.model).all()
    def get_by_username(self, username -> str):
        return (
            session.query(self.model)
            .filter_by(get_by_username=username)
            .first()
         )
    def get_by_email(self, email -> str):
        return (
            session.query(self.model)
            .filter_by(email=email)
            .first()
         )
user_dao = UserDAO(User)


app/routes/users.py
from flask import Blueprint, jsonfiy
from app.daos import user_dao
user_bp = Blueprint('user_bp', __name__)
@user_bp.route("/api/users", methods=["GET])
def get_users():
    return jsonify(user_dao.get_all())