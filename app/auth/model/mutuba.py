from instance import db

class Mutuba(db.Model):
    
    __tablename__ = 'mutuba'
    
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)