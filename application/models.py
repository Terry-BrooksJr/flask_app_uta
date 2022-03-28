from application import app, db_NoSQL
from werkzeug.security import generate_password_hash, check_password_hash

class User(db_NoSQL.Document):
    user_id = db_NoSQL.IntField(unique=True)
    first_name = db_NoSQL.StringField(max_length=50)
    last_name = db_NoSQL.StringField(max_length=50)
    email = db_NoSQL.StringField(max_length=30, unique=True)
    password = db_NoSQL.StringField(max_length=50)

def set_password(self, password):
    self.password = generate_password_hash(password)


def get_password(self, password):
    self.password = check_password_hash(self.password,password)

class Courses(db_NoSQL.Document):
    course_id = db_NoSQL.IntField(unique=True, max_length=10)
    title = db_NoSQL.StringField(max_length=50)
    description = db_NoSQL.StringField(max_length=50)
    credits = db_NoSQL.StringField(max_length=30)
    term = db_NoSQL.StringField(max_length=50)


class Enrollment(db_NoSQL.Document):
    user_id = db_NoSQL.IntField(unique=True)
    course_id = db_NoSQL.IntField(unique=True)
    last_name = db_NoSQL.StringField(max_length=50)
    email = db_NoSQL.StringField(max_length=30)
    password = db_NoSQL.StringField(max_length=50)
