
from sqlalchemy.dialects.postgresql import ARRAY
from instance import db
class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    parent_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    parent = db.relationship('Tag', remote_side=[id], backref='children')
    text_array = db.Column(ARRAY(db.String))    
    # makes sense for product and product variations