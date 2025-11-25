from flask import Flask
from config import Config
import os
from extensions import db, bcrypt
from controllers.user_controller import user_bp
from controllers.teacher_controller import teacher_bp
from controllers.admin_controller import admin_bp
from controllers import controllers

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))

app.config['UPLOAD_FOLDER'] = os.path.join("uploads", "assignments")

app.config.from_object(Config)

for controller in controllers:
    app.register_blueprint(controller)

db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)