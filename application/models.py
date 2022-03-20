class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=50)


class Courses(db.Document):
    course_id = db.IntField(unique=True)
    title = db.StringField(max_length=50)
    description = db.StringField(max_length=50)
    credits = db.StringField(max_length=30)
    term = db.StringField(max_length=50)


class Enrollment(db.Document):
    user_id = db.IntField(unique=True)
    course_id = db.IntField(unique=True)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=50)
