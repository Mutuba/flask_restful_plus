
from instance import db

category_tree = db.Table(
    'category_tree', 
    db.Column('parent_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('children_id', db.Integer, db.ForeignKey('category.id'))
)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    children = db.relationship(
        'Category', 
        secondary=category_tree,
        primaryjoin=(category_tree.c.parent_id == id),
        secondaryjoin=(category_tree.c.children_id == id),
        backref=db.backref('parents', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Category> {}'.format(self.id)
    
    
    # a child has a list of parents
    # a parent has a list of children