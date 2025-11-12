from extensions import db

class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade_worth = db.Column(db.Integer, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classrooms.id'), nullable=False)

    teacher = db.relationship('User', backref='assignments')
    classroom = db.relationship('Classroom', backref='assignments')