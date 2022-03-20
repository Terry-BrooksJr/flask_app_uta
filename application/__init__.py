from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=59999,debug=True)