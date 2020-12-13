
from instance import db

from .employee import Employee

class Engineer(Employee):
    __tablename__ = 'engineer'
    id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)
    engineer_name = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_identity':'engineer',
    }
    def __repr__(self):
        return f'Engineer {self.engineer_name}'