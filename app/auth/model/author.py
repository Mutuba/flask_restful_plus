from instance import db
from sqlalchemy_json import MutableJson

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    handles = db.Column(MutableJson)
    
    @staticmethod
    def json_query(value):
        return Author.query.filter(Author.handles['twitter'].astext == value).first()