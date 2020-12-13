from instance import db

from .employee import Employee


class Boss(Employee):
    __tablename__ = 'boss'
    id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)
    boss_name = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_identity':'boss',
    }
    
    def __repr__(self):
        return f'Boss {self.boss_name}'