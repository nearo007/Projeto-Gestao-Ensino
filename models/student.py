from . import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    born_date = db.Column(db.DateTime, nullable=False)
    #classroom_id = db.Column(db.Integer, db.ForeignKey('classrooms.id'), nullable=False)

    #classroom = db.relationship('Classroom', backref='classrooms')