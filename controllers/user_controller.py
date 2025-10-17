from flask import render_template, request, redirect, url_for, Blueprint
from database import db
from models import User, Student, Classroom, Assignment

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def index():
    users = User.query.all()
    students = Student.query.all()
    classrooms = Classroom.query.all()
    assignments = Assignment.query.all()

    return render_template("index.html", users=users, students=students, classrooms=classrooms, assignments=assignments)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/")

    return render_template("register.html")