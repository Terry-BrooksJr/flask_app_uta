from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db_NoSQL = MongoEngine()
db_NoSQL.init_app(app)
db_SQL = SQLAlchemy(app)


from application import routes

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=59999,debug=True)