
from instance import db
import re
from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property
from app.auth.model.category import Category
from sqlalchemy_utils import observes

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    # currency = db.Column(CurrencyType, default=Currency('KSH'))
    price = db.Column(db.Numeric(precision=9, scale=2))
    discount = db.Column(db.Numeric(precision=5), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category= db.relationship(Category, backref="products")
    slug = db.Column(db.String)
    
    _email = db.Column(db.String)

    @hybrid_property
    def email(self):
        return self._email


    @email.setter
    def email(self, email):
        self._email = email

    
    @observes('name')
    def compute_slug(self, name):
        """
        Computes the slug - shortened version of the title.
        :param title:  string, title to be shortened
        :return: string, resulting slug
        """
        self.slug = slugify(name)