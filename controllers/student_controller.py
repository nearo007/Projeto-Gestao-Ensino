from flask import render_template, request, redirect, url_for, Blueprint
from models import db
from models.student import Student
from datetime import datetime

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        born_date_string = request.form['born_date']
        born_date = datetime.strptime(born_date_string, '%Y-%m-%d').date()

        new_student = Student(name=name, born_date=born_date)
        db.session.add(new_student)
        db.session.commit()

        return redirect("/")

    return render_template("add_student.html")