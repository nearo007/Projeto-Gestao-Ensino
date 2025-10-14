from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .employee import Employee
from .role import Role
from .skill import Skill
from .associations import role_skills # associa as duas de cima (roles & skills)