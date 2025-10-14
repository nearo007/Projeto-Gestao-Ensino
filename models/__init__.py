from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .student import Student
#from .role import Role
#from .skill import Skill
#from .associations import role_skills # associa as duas de cima (roles & skills)