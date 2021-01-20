from instance import db
# from sqlalchemy_json import MutableJson
from sqlalchemy.dialects.postgresql import JSON

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    handles = db.Column(JSON)
    
    @staticmethod
    def json_query(value):
        return Book.query.filter(Book.handles['twitter'].astext == value).first()